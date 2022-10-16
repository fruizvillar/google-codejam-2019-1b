"""
This files aims to solve the problem 'you can go your own way' in Google Code Jam competition 2019
"""
from enum import Enum
from collections import defaultdict


class Direction(Enum):
    """ Maps the directions the maze solvers can take
    """
    SOUTH = 'S'
    EAST = 'E'
    NORTH = 'N'
    WEST = 'W'


class Case:
    """
    Maps a case in the problem
    """
    count = 0

    def __init__(self, p, q):
        Case.count += 1

        self.case_number = Case.count
        self.side = q
        self.people = p
        self.moving_towards = defaultdict(lambda: 0)
        self.most_visited = None

    def read_all_lines(self):
        """
        Solves the problem and stores the result in the instance
        Returns:

        """
        for i in range(self.people):
            values = input().split()
            x, y = [int(i) for i in values[:2]]
            towards = Direction(values[2])
            if towards == Direction.NORTH:
                for xi in range(self.side + 1):
                    for yi in range(y + 1, self.side + 1):
                        self.moving_towards[(xi, yi)] += 1
            elif towards == Direction.SOUTH:
                for xi in range(self.side + 1):
                    for yi in range(0, y):
                        self.moving_towards[(xi, yi)] += 1
            elif towards == Direction.EAST:
                for yi in range(self.side + 1):
                    for xi in range(x + 1, self.side + 1):
                        self.moving_towards[(xi, yi)] += 1
            elif towards == Direction.WEST:
                for yi in range(self.side + 1):
                    for xi in range(0, x):
                        self.moving_towards[(xi, yi)] += 1

    def find_most_visited(self):
        """ Finds the most visited point by checking all the destinations """
        towards_max = 0
        max_c = (0, 0)
        for (x, y), n in self.moving_towards.items():
            if n > towards_max:
                towards_max = n
                max_c = (x, y)
            elif n == towards_max:
                if x < max_c[0]:
                    max_c = (x, y)
                elif x == max_c[0]:
                    if y < max_c[1]:
                        max_c = (x, y)
        self.most_visited = max_c

    def __str__(self):
        return 'Case #{0.case_number}: {0.most_visited[0]} {0.most_visited[1]}'.format(self)


def main():
    """
    Main class. Reads input, solves the problem and prints the output.
    Returns:

    """
    t = int(input())  # number of test cases

    for _ in range(t):
        c = Case(*[int(i) for i in input().split()])  # first line: p, q
        c.read_all_lines()
        c.find_most_visited()
        print(c)


if __name__ == '__main__':
    main()

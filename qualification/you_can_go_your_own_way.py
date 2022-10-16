"""
This files aims to solve the problem 'you can go your own way' in Google Code Jam competition 2019
"""
from enum import Enum
import cProfile

PROFILE = False


class Direction(Enum):
    """ Maps the directions the maze solvers can take
    """
    SOUTH = 'S'
    EAST = 'E'


class Coord:
    """
    Represents a coordinate, being the northwesternmost point the origin and x y from W to E and N to S respectively.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Coord(-self.x, -self.y)

    def __str__(self):
        return '({0.x}, {0.y})'.format(self)


class Step:
    """
    Maps a step taken when solving the maze. Can be backwards (undo) if a non-exit point is found.
    """

    def __init__(self, orig, direction, undo=False):
        self.orig = orig
        self.direction = direction
        self.undo = undo
        vector = Coord(1, 0) if direction == Direction.EAST else Coord(0, 1)
        if undo:
            vector = -vector
        self.dest = orig + vector

    def __eq__(self, other):
        if isinstance(other, Step):
            return self.orig == other.orig and self.dest == other.dest
        return False

    def __neg__(self):
        return Step(self.dest, self.direction, not self.undo)

    def __str__(self):
        if self.undo:
            return '{0.dest} <-{0.direction}-- {0.orig}'.format(self)
        return '{0.orig} --{0.direction}-> {0.dest}'.format(self)

    def __repr__(self):
        return '{{{0.orig}->{0.dest}}}'.format(self)


class Case:
    """
    Maps a case in the problem
    """
    count = 0

    def __init__(self, side, lydias_path):
        Case.count += 1

        self.case_number = Case.count
        self.side = side
        self.last_step_was_southbound = False
        self.pos = Coord(0, 0)
        self.final_pos = Coord(side - 1, side - 1)
        self.lydias_path = lydias_path
        self.wrong_steps = []
        self.my_path = []
        self.step_number = 0
        self.e_in_my_path = 0
        self.e_in_lydias_path = 0

        self.solve()
        print(self)

    def solve(self):
        """
        Solves the problem and stores the result in the instance
        Returns:

        """
        if True:
            self.my_path = (self.lydias_path.replace('S', 'X',)
                            .replace('E', 'S')
                            .replace('X', 'E'))
            return
        while self.step_number < 2 * self.side - 2:
            lydias_next_dir = Direction(self.lydias_path[self.step_number])

            step_south = Step(self.pos, Direction.SOUTH)
            step_east = Step(self.pos, Direction.EAST)

            south_doable = self._step_is_doable(step_south, lydias_next_dir)
            east_doable = self._step_is_doable(step_east, lydias_next_dir)

            if south_doable and east_doable:
                if Direction(self.my_path[-1]) == Direction.EAST:
                    self._take_step(step_south)
                else:
                    self._take_step(step_east)

            elif south_doable:
                self._take_step(step_south)

            elif east_doable:
                self._take_step(step_east)

            else:

                self._undo_last_step()
                if lydias_next_dir == Direction.EAST:
                    self.e_in_lydias_path -= 1

            if lydias_next_dir == Direction.EAST:
                self.e_in_lydias_path += 1

    def _step_is_doable(self, step, lydias_next_dir):
        if self._pos_is_out(step.dest):
            return False

        if self._step_has_being_done_by_lydia(step, lydias_next_dir):
            return False

        if step in self.wrong_steps:
            return False
        return True

    def _step_has_being_done_by_lydia(self, step, lydias_next_dir):
        if step.direction != Direction(lydias_next_dir):
            return False
        if self.step_number == 0:
            return True

        return self.e_in_lydias_path == self.e_in_my_path

    def _take_step(self, step, undo=False):
        self.pos = step.dest
        if undo:
            self.step_number -= 1
        else:
            self.my_path.append(str(step.direction.value))
            self.step_number += 1
            if step.direction == Direction.EAST:
                self.e_in_my_path += 1

    def _undo_last_step(self):
        towards = Direction(self.my_path.pop())

        if towards == Direction.EAST:
            self.e_in_my_path -= 1

        step_back = Step(self.pos, towards, undo=True)
        self.wrong_steps.append(-step_back)
        self._take_step(step_back, undo=True)

    def _pos_is_out(self, pos):
        return not (0 <= pos.x < self.side and 0 <= pos.y < self.side)

    def __str__(self):
        return 'Case #{0.case_number}: {1}'.format(self, ''.join(self.my_path))


def main():
    """
    Main class. Reads input, solves the problem and prints the output.
    Returns:

    """
    t = int(input())  # number of test cases

    for _ in range(t):
        Case(int(input()), input())  # first line: dim; second line: Lydia's path


if __name__ == '__main__':
    if PROFILE:
        cProfile.run('main()')
    else:
        main()

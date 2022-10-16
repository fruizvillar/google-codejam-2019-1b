"""
This files aims to solve the problem 'foregone solution' in Google Code Jam competition 2019
"""
BROKEN_KEY = '4'


class Case:
    """
    Maps a case in the problem
    """
    count = 0

    def __init__(self, amount):
        self.n = Case.count + 1
        Case.count += 1
        self.amount = amount
        self.x1 = None
        self.x2 = None

    def solve(self):
        """
        Solves the problem and stores the result in the instance
        Returns:

        """
        if self.x1:
            return

        x1 = self.amount
        x2 = 0

        try:
            while True:
                x1_repr = str(x1)
                pos_from_left = x1_repr.find(BROKEN_KEY)

                if pos_from_left != -1:
                    pos_from_right = len(x1_repr) - pos_from_left - 1

                    variation = 10 ** pos_from_right
                    x1 -= variation
                    x2 += variation
                    continue

                x2_repr = str(x2)
                x2_repr.index(BROKEN_KEY)  # If not found, a exception will be raised and we're done

                # Otherwise we iterate one by one
                variation = 1
                x1 -= variation
                x2 += variation

        except ValueError:
            self.x1 = x1
            self.x2 = x2

    def __str__(self):
        return 'Case #{0.n}: {0.x1} {0.x2}'.format(self)


def main():
    """
    Main class. Reads input, solves the problem and prints the output.
    Returns:

    """
    cases = read_input()

    for c in cases:
        c.solve()
        print(c)


def read_input():
    """
    Reads the input in the specified format.

    Returns: a list of Case, each of them is

    """
    n = int(input())  # read a line with a single integer

    return [Case(int(input())) for _ in range(n)]


if __name__ == '__main__':
    main()

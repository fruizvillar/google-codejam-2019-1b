"""
This files aims to solve the problem 'you can go your own way' in Google Code Jam competition 2019
"""


class Case:
    """
    Maps a case in the problem
    """
    count = 0

    def __init__(self, n, k, ci, di):
        Case.count += 1

        self.case_number = Case.count
        self.n_swords = n
        self.fair_diff = k
        self.c_skills = ci
        self.d_skills = di
        self.n_fair_assaults = 0

    def find_n_fair_assaults(self):
        """ Finds the most visited point by checking all the destinations """
        for l in range(self.n_swords):
            for r in range(l, self.n_swords):
                c_max = max(self.c_skills[l:r+1])
                d_max = max(self.d_skills[l:r+1])
                if abs(c_max - d_max) <= self.fair_diff:
                    self.n_fair_assaults += 1

    def __str__(self):
        return 'Case #{0.case_number}: {0.n_fair_assaults}'.format(self)


def main():
    """
    Main class. Reads input, solves the problem and prints the output.
    Returns:

    """
    t = int(input())  # number of test cases

    for _ in range(t):
        c = Case(*[int(i) for i in input().split()],  # first line: n, k
                 [int(i) for i in input().split()],  # second line: Ci
                 [int(i) for i in input().split()])  # third line: Di
        c.find_n_fair_assaults()
        print(c)


if __name__ == '__main__':
    main()

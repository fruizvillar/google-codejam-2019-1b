"""
Solves the problem DAT BAE (Code Jam 2019)
"""
import sys

import numpy as np


class Case:
    n_cases = 0

    def __init__(self, w):
        Case.n_cases += 1
        self.n_case = Case.n_cases
        self.w = w
        self.iterations = []
        self.solution = [0, 0, 0, 0, 0, 0]

    def make_hints(self):
        for i in range(self.w):
            day_attempt = i + 1
            print(str(day_attempt), flush=True)
            self.iterations.append(int(input()))

    def get_solution(self):
        # D0      [1, 1, 1, 1, 1, 1]
        matrix = [[2, 1, 1, 1, 1, 1],
                  [4, 2, 1, 1, 1, 1],
                  [8, 2, 2, 1, 1, 1],
                  [16, 4, 2, 2, 1, 1],
                  [32, 4, 2, 2, 2, 1],
                  [64, 8, 4, 2, 2, 2]]

        b = self.iterations
        sol = np.linalg.solve(matrix, b)
        self.solution = [int(round(i)) for i in sol]
    def send_solution(self):
        print(*self.solution, flush=True)
        return int(input())

    def __str__(self):
        return '{0.n_case}: B={0.b}, F={0.f}, N={0.n}'.format(self)


def main():
    t, w = [int(i) for i in input().split(' ')]  # number of test cases, number of guesses
    for _ in range(t):
        case = Case(w)
        case.make_hints()
        case.get_solution()
        verdict = case.send_solution()
        if verdict != 1:
            break


def read_input_int():
    line = [int(i) for i in input().split(' ')]
    return (line[0], line[1], line[2])


if __name__ == '__main__':
    main()

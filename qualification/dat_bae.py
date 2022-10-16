"""
Solves the problem DAT BAE (Code Jam 2019)
"""
import sys


class Case:
    n_cases = 0

    def __init__(self, params):
        Case.n_cases += 1
        self.n_case = Case.n_cases
        self.n, self.b, self.f = params
        self.iterations = {}
        self.solution = None

    def make_hints(self):
        for i in range(min(self.n, self.f)):
            attempt = '{{:0{}d}}'.format(self.n).format(10 ** i)
            print(attempt, flush=True)
            self.iterations[self.n - i - 1] = int(input()) > 0

    def get_solution(self):
        solution = []
        for k, v in self.iterations.items():
            if not v:
                solution.append(k)
        self.solution = ' '.join((str(i) for i in sorted(solution)))

    def send_solution(self):
        print(self.solution, flush=True)
        return int(input())

    def __str__(self):
        return '{0.n_case}: B={0.b}, F={0.f}, N={0.n}'.format(self)

def main():
    t = int(input())  # number of test cases
    for _ in range(t):
        case = Case(read_input_int())
        print(case.f, case.b, case.n, file=sys.stderr, flush=True)
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

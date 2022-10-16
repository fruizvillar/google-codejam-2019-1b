"""
This files aims to solve the problem 'cryptopangrams' in Google Code Jam competition 2019
"""
import math
import cProfile

PROFILE = False

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def first_factor(n, possible_factors):
    for f in possible_factors:
        if n % f == 0:
            return f

    return None
class Case():
    def __init__(self, i, n, size, numbers):
        self.i = i
        self.n = n
        self.size = size
        self.numbers = numbers
        self.message = self._decode()
        print(self)

    def _decode(self):
        """
    
        Returns:

        """
        primes_generator = (n for n in range(2, self.n + 1) if is_prime(n))

        message_encoded = []

        first_number = self.numbers[0]
        factor1 = first_factor(first_number, primes_generator)
        factor2 = first_number // factor1

        previous_factor = factor2 if self.numbers[1] % factor1 == 0 else factor1
        message_encoded.append(previous_factor)

        for n in self.numbers:
            new_factor = n // previous_factor
            print('{} * {} = {}'.format(new_factor, previous_factor, n))
            message_encoded.append(new_factor)
            previous_factor = new_factor

        cypher_map = {}
        char = 'A'
        for n in sorted(set(message_encoded)):
            cypher_map[n] = char
            char = chr(ord(char) + 1)

        return [cypher_map[n] for n in message_encoded]

    def __str__(self):
        return 'Case #{0.i}: {1}'.format(self, ''.join([str(i) for i in self.message]))


def main():
    """
    Main class. Reads input, solves the problem and prints the output.
    Returns:

    """
    t = int(input())  # number of test cases

    for i in range(1, t + 1):
        # first line: max_prime; n_numbers line: numbers
        Case(i, *[int(n) for n in input().split(' ')], [int(n) for n in input().split(' ')])


if __name__ == '__main__':
    if PROFILE:
        cProfile.run('main()')
    else:
        main()

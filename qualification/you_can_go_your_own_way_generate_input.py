import shutil
from pathlib import Path
import random
DEFAULT_INPUT = 'you_can_go_your_own_way_input_test_default.txt'

INPUT = 'you_can_go_your_own_way_input_test.txt'
USE_DEFAULT = False

T = 100
N = 10000


def main():
    if USE_DEFAULT:
        shutil.copy(DEFAULT_INPUT, INPUT)
    else:
        with Path(INPUT).open('w') as f:
            f.write('{}\n'.format(T))
            for n in range(T):
                f.write('{}\n'.format(N))
                sequence = ''.join([random.choice(['E', 'S']) for _ in range(2 * N - 2)])
                es = len([e for e in sequence if e == 'E'])
                if es > N - 1:
                    sequence = sequence.replace('E', 'S', es - N + 1)
                else:
                    sequence = sequence.replace('S', 'E', N - 1 - es)
                f.write(sequence + '\n')
    print('Generated')


if __name__ == '__main__':
    main()

"""
This files measures the elapsed time when solving a problem
"""

from datetime import datetime

import you_can_go_your_own_way


def main():
    """

    Returns:

    """
    start = datetime.now()
    print('Start', start)
    you_can_go_your_own_way.main()
    print('Took', datetime.now() - start)


if __name__ == '__main__':
    main()

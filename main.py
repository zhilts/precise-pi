#!./venv/bin/python
import sys

from pi_rand import pi_rand
from pi_row import pi_row
from pi_sqr import pi_sqr


def process(algorithm, delta):
    if algorithm == 'sqr':
        return pi_sqr(delta)
    if algorithm == 'rand':
        return pi_rand(delta)
    if algorithm == 'row':
        return pi_row(delta)
    print('Invalid algorithm')
    exit(2)


if __name__ == '__main__':
    _, algorithm, delta_str, *_ = sys.argv
    delta = float(delta_str)
    res = process(algorithm, delta)

    print(res)

from random import random

from output import print_iteration


def pi_rand(delta):
    inside, total = 0, 1
    while (inside + 1) * 4 / total - inside * 4 / total > delta:
        x, y = random(), random()
        if x * x + y * y <= 1:
            inside += 1
        total += 1
        print_iteration(inside * 4 / total, (inside + 1) * 4 / total)
    return (2 * inside + 1) * 4 / 2 / total

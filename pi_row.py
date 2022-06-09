from output import print_iteration


def pi_row(delta):
    value = 4
    divider = 3
    top, bottom = 4, 1
    sign = -1
    while top - bottom > delta:
        prev_value = value
        value += sign * 4 / divider
        sign *= -1
        divider += 2
        top = max(value, prev_value)
        bottom = min(value, prev_value)
        print_iteration(bottom, top)

    return (top + bottom) / 2

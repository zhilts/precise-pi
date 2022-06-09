def int_iteration():
    counter = 0
    while True:
        counter += 1
        yield counter


counter_generator = int_iteration()


def print_iteration(bottom, top):
    delta = top - bottom
    print('{index:5d} {bottom:.7f} - {top:.7f} d={delta:.9f}'.format(
        index=next(counter_generator),
        bottom=bottom,
        top=top,
        delta=delta)
    )

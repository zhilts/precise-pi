from output import print_iteration


def pi_sqr(delta):
    top, bottom, segments = 1, 0, 1
    squares = segments * segments

    points = [(0, 0)]

    while top * 4 / squares - bottom * 4 / squares > delta:
        new_segments = segments * 2
        bottom *= 4
        new_points = []
        new_squares = new_segments * new_segments
        for x, y in points:
            step_points = [
                (x * 2, y * 2),
                (x * 2 + 1, y * 2),
                (x * 2, y * 2 + 1),
                (x * 2 + 1, y * 2 + 1),
            ]
            for point in step_points:
                borders = get_borders(point, new_squares)
                if borders < 0:
                    bottom += 1
                elif borders == 0:
                    new_points.append(point)

        top = bottom + len(new_points)

        points = new_points
        squares = new_squares
        segments = new_segments
        print_iteration(bottom * 4 / squares, top * 4 / squares)

    return 4 * (top + bottom) / (2 * segments * segments)


def get_borders(point, square_len):
    x, y = point
    x2, y2 = x + 1, y + 1
    if x * x + y * y > square_len:
        return 1
    if x2 * x2 + y2 * y2 < square_len:
        return -1
    return 0

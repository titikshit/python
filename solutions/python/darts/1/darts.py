def score(x, y):
    circle_rad_square = x ** 2 + y ** 2

    if circle_rad_square <= 1:
        return 10

    if circle_rad_square <= 25:
        return 5

    if circle_rad_square <= 100:
        return 1

    else:
        return 0
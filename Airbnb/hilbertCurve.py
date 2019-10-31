def hilbertCurve(x, y, iter):
    if not iter:
        return 1
    len = 1 << (iter - 1)
    num = 1 << (2 * (iter - 1))
    if x >= len and y >= len:  # 3 Shape is identical with previous iteration
        return 2 * num + hilbertCurve(x - len, y - len, iter - 1)
    elif x < len and y >= len:  # 2 Shape is identical with previous iteration
        return num + hilbertCurve(x, y - len, iter - 1)
    elif x < len and y < len:  # 1 Clock-wise rotate 90
        return hilbertCurve(y, x, iter - 1)
    else:  # 4 Anti-Clockwise rotate 90
        return 3 * num + hilbertCurve(len - y - 1, 2 * len - x - 1, iter - 1)


assert 3 == hilbertCurve(1, 1, 2)
assert 2 == hilbertCurve(0, 1, 1)
assert 9 == hilbertCurve(2, 2, 2)

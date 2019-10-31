def numberofIntersectedRectangles(rect):
    if not rect:
        return 0

    def intersect(r1, r2):
        return r1[0][0] < r2[0][0] and r1[0][1] < r2[0][1] and r2[0][0] < r1[1][0] and r2[0][1] < r1[1][1] or r1[0][0] < \
                                                                                                              r2[1][
                                                                                                                  0] and \
                                                                                                              r1[0][1] < \
                                                                                                              r2[1][
                                                                                                                  1] and \
                                                                                                              r2[1][0] < \
                                                                                                              r1[1][
                                                                                                                  0] and \
                                                                                                              r2[1][1] < \
                                                                                                              r1[1][1]

    p = {}

    def find(x):
        while x != p[x]:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(x, y):
        p.setdefault(x, x)
        p.setdefault(y, y)
        p[find(x)] = find(y)

    for i in range(len(rect)):
        for j in range(i + 1, len(rect)):
            if intersect(rect[i], rect[j]):
                union(rect[i], rect[j])

    return len({find(x) for x in rect})


print(numberofIntersectedRectangles([((-3, -2), (2, 1)),
                                     ((10, 8), (15, 10)),
                                     ((1, 0), (7, 4)),
                                     ((12, 9), (16, 12)),
                                     ((-2, -1), (5, 3))]))

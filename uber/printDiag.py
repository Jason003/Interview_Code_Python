import collections


def solution(A):
    if not A:
        return []
    m, n = len(A), len(A[0])
    d = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            d[i - j].append(A[i][j])
    res = []
    for k in sorted(list(d.keys()), reverse=True):
        res.extend(d[k])
    return res


print(solution([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 0],
                [1, 2, 3, 4, 5]]))

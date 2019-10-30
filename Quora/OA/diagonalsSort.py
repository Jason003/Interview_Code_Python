import collections


def diagonalsSort(A):
    if not A: return A
    d = collections.defaultdict(list)
    m, n = len(A), len(A[0])
    for i in range(m):
        for j in range(n):
            d[i - j].append(A[i][j])
    for i in d:
        d[i].sort(reverse = True)
    for i in range(m):
        for j in range(n):
            A[i][j] = d[i - j].pop()
    return A


print(diagonalsSort([[8, 4, 1], [4, 4, 1], [4, 8, 9]]))

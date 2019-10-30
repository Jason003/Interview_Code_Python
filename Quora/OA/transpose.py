def solution(A):
    n = len(A)
    d = {(i, j) : A[i][j] for i in range(n) for j in range(n) if i == j or i + j == n - 1}
    for i in range(n):
        for j in range(i + 1):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(n):
        l, r = 0, n - 1
        while l < r:
            A[i][l], A[i][r] = A[i][r], A[i][l]
            l += 1
            r -= 1
    for i, j in d:
        A[i][j] = d[i, j]
    return A

print(solution([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]))
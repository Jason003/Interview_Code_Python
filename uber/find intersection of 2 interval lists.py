def solution(A, B):
    A.sort()
    B.sort()
    i, j = 0, 0
    m, n = len(A), len(B)
    res = []
    while i < m and j < n:
        l = max(A[i][0], B[j][0])
        r = min(A[i][1], B[j][1])
        if l < r:
            res.append((l, r, A[i][2] and B[j][2]))
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return res

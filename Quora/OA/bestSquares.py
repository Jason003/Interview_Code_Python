def bestSquares(A, k):
    m, n = len(A), len(A[0])
    res = []
    mx = 0
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            cur = [A[x][y] for x in range(i, i + k) for y in range(j, j + k)]
            summ = sum(cur)
            if summ > mx:
                res = cur
                mx = summ
            elif summ == mx:
                res += cur
    return sum(set(res))
print(bestSquares([[1,2,4],[6,5,5],[3,2,1]], 2))

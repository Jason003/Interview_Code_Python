def ribbon(A, k):
    def judge(m):
        res = 0
        for a in A:
            res += a // m
        return res >= k
    lo, hi = 1, max(A)
    res = 0
    while lo <= hi:
        m = (lo + hi) // 2
        if judge(m):
            res = max(res, m)
            lo = m + 1
        else:
            hi = m - 1
    return res
print(ribbon([1,2,3,4,9], 5))

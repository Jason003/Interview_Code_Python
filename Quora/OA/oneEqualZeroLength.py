def solution(A):
    A = [-1 if a == 0 else 1 for a in A]
    d = {0 : -1}
    cur = 0
    res = 0
    for i, a in enumerate(A):
        cur += a
        if cur in d:
            res = max(res, i - d[cur])
        d.setdefault(cur, i)
    return res

print(solution([1,0]))
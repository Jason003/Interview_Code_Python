import collections
def solution(a, b):
    cnt = collections.Counter()
    for s, e in a + b:
        cnt[s] += 1
        cnt[e] -= 1
    res = []
    pre = -1
    curSum = 0
    preSum = 0
    for t in sorted(list(cnt.keys())):
        curSum += cnt[t]
        if preSum == 1 and curSum != 1:
            res.append((pre, t))
        pre = t
        preSum = curSum
    return res
a = [[1, 5], [7, 10], [12,14]]
b = [[2, 6], [10, 10]]
print(solution(a, b))
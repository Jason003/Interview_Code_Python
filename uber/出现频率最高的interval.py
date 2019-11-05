import collections
def solution(A):
    record = collections.Counter()
    for s, e in A:
        record[s] += 1
        record[e] -= 1
    curr = 0
    res = []
    max_freq = 0
    pre = None
    d = {}
    for t in sorted(list(record.keys())):
        curr += record[t]
        d[t] = curr
        max_freq = max(curr, max_freq)
    for t in sorted(list(d.keys())):
        if d[t] == max_freq:
            if pre:
                res.append((pre, t))
            pre = t
        elif pre:
            res.append((pre, t))
            pre = None
    return res

print(solution([[1,2],[3,4],[4,7],[7,8],[3,8],[5,6]]))

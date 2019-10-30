import collections
def coolFeature(a, b, query):
    query = [q[1:] for q in query]
    cnta, cntb = collections.Counter(a), collections.Counter(b)

    def judge(n):
        res = 0
        for i in cnta:
            res += cnta[i] * cntb[n - i]
        return res

    res = []

    for q in query:
        if len(q) == 1:
            res.append(judge(q[0]))
        else:
            cntb[b[q[0] - 1]] -= 1
            cntb[q[1]] += 1
    return res
print(coolFeature([1,2,3], [3, 4], [[1, 5], [1, 1, 1], [1, 5]]))
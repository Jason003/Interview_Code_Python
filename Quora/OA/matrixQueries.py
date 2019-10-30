import collections
import bisect
def matrixQueries(A, Q):
    n = len(A)
    cnt = collections.defaultdict(list)
    for i, a in enumerate(A):
        cnt[a].append(i)
    res = []
    for l, r, t in Q:
        tep = bisect.bisect_right(cnt[t], r) - bisect.bisect_left(cnt[t], l)
        res.append(tep)
    return res

def bruteForce(A, Q):
    res = []
    for l, r, t in Q:
        res.append(sum([i == t for i in A[l : r+1]] or [0]))
    return res

import random

A = [random.randint(0, 1000) for _ in range(1000)]
for _ in range(100):
    Q = []
    for _ in range(100):
        i = random.randint(0, 999)
        j = random.randint(i, 999)
        t = A[i]
        Q.append((i, j, t))
    print(matrixQueries(A, Q) == bruteForce(A, Q))

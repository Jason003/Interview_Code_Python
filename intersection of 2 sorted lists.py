import random
import collections
def combine(A, B):
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            res.append(A[i])
            i += 1
            j += 1

        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return res

for _ in range(100):
    A = sorted([random.randint(0, 100) for _ in range(100)])
    B = sorted([random.randint(0, 100) for _ in range(100)])
    cntA = collections.Counter(A)
    cntB = collections.Counter(B)
    inter = cntA & cntB
    assert combine(A, B) == sorted(list(inter.elements()))
import random
def findMedian(A):
    if not A:
        return
    n = len(A)

    def quickSelect(k, l = 0, r = n - 1):
        if l >= r:
            return A[l]
        p = l
        for i in range(l, r):
            if A[i] <= A[r]:
                A[p], A[i] = A[i], A[p]
                p += 1
        A[p], A[r] = A[r], A[p]
        if p == k:
            return A[p]
        elif p > k:
            return quickSelect(k, l, p - 1)
        else:
            return quickSelect(k, p + 1, r)

    if n % 2 == 1:
        return quickSelect(n // 2)
    else:
        return (quickSelect(n // 2) + quickSelect(n // 2 - 1)) / 2

for _ in range(100):
    A = []
    for _ in range(100):
        A.append(random.randint(0, 100))
    assert (sorted(A)[len(A) // 2] + sorted(A)[len(A) // 2 - 1]) / 2 == (findMedian(A))
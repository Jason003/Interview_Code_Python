def findMedian(A):
    def findKth(A, k):
        hi, lo = 2 ** 31 - 1, -2 ** 31
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            cnt = 0
            for a in A:
                if a <= mi:
                    cnt += 1
            if cnt < k:
                lo = mi + 1
            else:
                hi = mi
        return lo
    n = len(A)
    if n % 2 == 1:
        return findKth(A, n // 2 + 1)
    else:
        return (findKth(A, n // 2) + findKth(A, n // 2 + 1)) / 2

import random
for _ in range(1000):
    A = sorted([random.randint(0, 100) for _ in range(random.randint(10, 100))])
    median = sorted(A)[len(A) // 2] if len(A) % 2 == 1 else (sorted(A)[len(A) // 2] + sorted(A)[len(A) // 2 - 1]) / 2
    assert findMedian(A) == median

# quick select, can't work for this problem
# import random
# def findMedian(A):
#     if not A:
#         return
#     n = len(A)
#
#     def quickSelect(k, l = 0, r = n - 1):
#         if l >= r:
#             return A[l]
#         p = l
#         for i in range(l, r):
#             if A[i] <= A[r]:
#                 A[p], A[i] = A[i], A[p]
#                 p += 1
#         A[p], A[r] = A[r], A[p]
#         if p == k:
#             return A[p]
#         elif p > k:
#             return quickSelect(k, l, p - 1)
#         else:
#             return quickSelect(k, p + 1, r)
#
#     if n % 2 == 1:
#         return quickSelect(n // 2)
#     else:
#         return (quickSelect(n // 2) + quickSelect(n // 2 - 1)) / 2
#
# for _ in range(100):
#     A = []
#     for _ in range(100):
#         A.append(random.randint(0, 100))
#     assert (sorted(A)[len(A) // 2] + sorted(A)[len(A) // 2 - 1]) / 2 == (findMedian(A))
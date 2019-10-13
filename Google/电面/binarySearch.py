import math
def left_most(A, target):
    i, j = 0, len(A) - 1
    while i < j:
        m = (j - i) // 2 + i
        if A[m] < target:
            i = m + 1
        else:
            j = m
    return i

def right_most(A, target):
    i, j = 0, len(A) - 1
    while i < j:
        m = math.ceil((j + i) / 2)
        if A[m] > target:
            j = m - 1
        else:
            i = m
    return i

print(right_most([1,2,2,2,2,2], 2))

# [1,1,1,2,2,4] 1
import random
for _ in range(100):
    A = sorted([random.randint(0, 10) for _ in range(100)])
    target = A[50]
    time = right_most(A, target) - left_most(A, target) + 1
    print(time == A.count(target))
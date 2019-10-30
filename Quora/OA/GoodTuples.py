import collections
def GoodTuples(A):
    res = 0
    for i in range(len(A) - 2):
        cnt = collections.Counter(A[i:i+3])
        if len(set(cnt.values())) == 2:
            res += 1
    return res
print(GoodTuples([1, 1, 2, 1, 5, 3, 2, 3]))

def different(A):
    res = 0
    for i in range(len(A) - 2):
        cnt = collections.Counter(A[i:i+3])
        if len(set(cnt.values())) == 1:
            res += 1
    return res
print(different("aabdcreff"))
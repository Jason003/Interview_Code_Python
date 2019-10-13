import collections
def solution(A, k):
    n = len(A)
    if n % k != 0:
        return 'No'
    cnt = collections.Counter(A)
    for v in cnt.values():
        if v > k:
            return 'No'
    return 'Yes'

print(solution([1,2,3,3], 3))
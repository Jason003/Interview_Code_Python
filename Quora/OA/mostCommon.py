import collections
def solution(A):
    if not A: return []
    cnt = collections.Counter(A)
    mx = max(cnt.values())
    return [i for i in cnt if cnt[i] == mx]
print(solution([2,2,3,3,5]))
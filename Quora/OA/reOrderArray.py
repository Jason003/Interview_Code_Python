import collections
def solution(A):
    n = len(A)
    arr = [A[i][j] for i in range(n) for j in range(n)]
    cnt = collections.Counter(arr)
    arr.sort(key = lambda x : (cnt[x], x))
    k = 0
    while arr:
        for i in range(k + 1):
            if 0 <= i < n and 0 <= k - i < n:
                A[i][k - i] = arr.pop()
        k += 1
    return A

print(solution([[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]))
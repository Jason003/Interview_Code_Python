def solution(n, k):
    k -= 1
    i = k
    A = list(range(1, n + 1))
    res = []
    while len(A) > 1:
        res.append(A.pop(i))
        i = (i + k) % (len(A))
    return res

print(solution(5, 3))
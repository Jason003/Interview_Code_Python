def solution(A):
    n = len(A)
    dp = [0] * (n + 1) # dp[i] means the biggest sum till i
    res = 0
    for i, a in enumerate(A):
        dp[i + 1] = max((dp[i - 1] if i > 0 else 0) + a, dp[i])
        res = max(res, dp[i + 1])
    return res

print(solution([1,2,3,4,5,6,7]))
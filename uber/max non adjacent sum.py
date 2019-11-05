def solution(A):
    n = len(A)
    dp = [0] * n
    for i, a in enumerate(A):
        dp[i] = max((dp[i - 2] if i > 1 else 0) + a, dp[i - 1] if i > 0 else 0)
    return dp[-1]

print(solution([3,4,1,2,3,1,5,7]))

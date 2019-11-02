'''
https://www.geeksforgeeks.org/find-if-string-is-k-palindrome-or-not/
'''
def solution(s, k):
    mem = {}
    def dfs(l, r):
        if l >= r:
            return 0
        if (l, r) in mem:
            return mem[l, r]
        if s[l] != s[r]:
            res = min(dfs(l + 1, r), dfs(l, r - 1)) + 1
        else:
            res = dfs(l + 1, r - 1)
        mem[l, r] = res
        return res
    return dfs(0, len(s) - 1) <= k

print(solution('abc', 2))
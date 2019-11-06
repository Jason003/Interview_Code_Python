
class Solution:
    def movesToStamp(self, s, t):
        s, t = list(s), list(t)
        m, n = len(s), len(t)
        res = []
        def check(i):
            change = False
            for j in range(m):
                if t[i + j] == '*': continue
                if t[i + j] != s[j]: return False
                change = True
            if change:
                t[i : i + m] = ['*'] * m
                res.append(i)
            return change
        found = True
        while found:
            found = False
            for i in range(n - m + 1):
                found |= check(i)
                if found: break
        return [] if t.count('*') != n else res[::-1]
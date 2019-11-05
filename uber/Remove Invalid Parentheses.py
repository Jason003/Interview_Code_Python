class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = [], []
        for i, c in enumerate(s):
            if c == '(':
                l.append(i)
            elif c == ')':
                if l:
                    l.pop()
                else:
                    r.append(i)
        toRemove = set(l + r)
        return ''.join([s[i] for i in range(len(s)) if i not in toRemove])


class Solution2:
    def removeInvalidParentheses(self, s: str):
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1

        res = set()
        '''
        idx: current index of s
        cur: current string
        l: extra left
        r: extra right
        p: net number of left parentheses
        '''

        def dfs(idx, cur, l, r, p):
            if idx == len(s):
                if l == r == p == 0:
                    res.add(cur)
                return
            if s[idx] == '(':
                if l > 0: dfs(idx + 1, cur, l - 1, r, p)
                dfs(idx + 1, cur + '(', l, r, p + 1)
            elif s[idx] == ')':
                if r > 0: dfs(idx + 1, cur, l, r - 1, p)
                if p > 0: dfs(idx + 1, cur + ')', l, r, p - 1)
            else:
                dfs(idx + 1, cur + s[idx], l, r, p)

        dfs(0, '', l, r, 0)
        return list(res)

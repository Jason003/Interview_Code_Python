def solution(m, n):
    res = set()

    def dfs(cur, i, j, stack): # n1 means the net '(' and n2 means the net '[', i means number of (), j means number of []
        if len(cur) == m + n:
            res.add(cur)
            return
        if not stack:
            if i > 0: dfs(cur + '(', i - 1, j, stack + ['('])
            if j > 0: dfs(cur + '[', i, j - 1, stack + ['['])
        else:
            if stack[-1] == '(':
                if i > 0: dfs(cur + '(', i - 1, j, stack + ['('])
                if j > 0: dfs(cur + '[', i, j - 1, stack + ['['])
                stack.pop()
                dfs(cur + ')', i, j, stack)
                stack.append('(')
            else:
                if i > 0: dfs(cur + '(', i - 1, j, stack + ['('])
                if j > 0: dfs(cur + '[', i, j - 1, stack + ['['])
                stack.pop()
                dfs(cur + ']', i, j, stack)
                stack.append('[')
    dfs('', m // 2, n // 2, [])
    return res
print(solution(2, 2))

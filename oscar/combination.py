def judge(a, b, c):
    mem = {}
    def dfs(i, j, k):
        if (i, j, k) in mem:
            return mem[i, j, k]
        if i == len(a) and j == len(b):
            if k == len(c):
                return True
            return False
        if i == len(a):
            res = c[k] == b[j]
        elif j == len(b):
            res = c[k] == a[i]
        elif c[k] == a[i] and c[k] == b[j]:
            res = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1)
        elif c[k] == a[i]:
            res = dfs(i + 1, j, k + 1)
        elif c[k] == b[j]:
            res = dfs(i, j + 1, k + 1)
        else:
            res = False
        mem[i, j, k] = res
        return res
    if len(a) + len(b) != len(c):
        return False
    return dfs(0, 0, 0)

print(judge('ab', 'ac', 'aabc'))

def boardScore(A):
    A = [a.split() for a in A]
    res = 0
    m, n = len(A), len(A[0])

    def dfs(i, j, flag):
        nonlocal score, area
        if i >= m or j >= n or i < 0 or j < 0 or not A[i][j] or A[i][j][0] != flag or A[i][j] == '#':
            return
        score += int(A[i][j][1:])
        area += 1
        A[i][j] = '#'
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(i + di, j + dj, flag)


    for i in range(m):
        for j in range(n):
            score = 0
            area = 0
            dfs(i, j, A[i][j][0])
            res += score * area
    return res

print(boardScore(["S0 W1 W1 W0 L2",
                "W0 W0 T0 T0 T0",
                "W0 W1 T0 M2 M1",
                "S0 L0 S1 S0 S0",
                "M0 R2 R0 S1 T0"]))
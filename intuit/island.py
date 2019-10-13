def find1(A, mark):
    if not A: return
    m, n = len(A), len(A[0])
    p1 = [float('inf'), float('inf')]
    p2 = [-1, -1]
    for i in range(m):
        for j in range(n):
            if A[i][j] == mark:
                p1[0] = min(p1[0], i)
                p1[1] = min(p1[1], j)
                p2[0] = max(p2[0], i)
                p2[1] = max(p2[1], j)
    print(p1 + p2)

# find1([[0, 0, 0],[0,0,0],[1,1,1]], 0)


def find2(A):
    if not A: return
    m, n = len(A), len(A[0])

    def dfs(i, j, mark):
        nonlocal A
        if i >= m or i < 0 or j >= n or j < 0 or A[i][j] != 0 or A[i][j] == mark: return
        A[i][j] = mark
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(i + di, j + dj, mark)

    mark = 2
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                dfs(i, j, mark)
                mark += 1
    for i in range(2, mark):
        find1(A, i)
find2([
[1,1,1,1,1,1],
[0,0,1,0,1,1],
[0,0,1,0,1,0],
[1,1,1,0,1,0],
[1,0,0,1,1,1]
])



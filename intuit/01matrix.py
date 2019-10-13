import collections

def surround(A, point):
    if not A: return
    m, n = len(A), len(A[0])
    x, y = point
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        xx, yy = x + dx, y + dy # neighbor of (x, y)
        if 0 <= xx < m and 0 <= yy < n and A[xx][yy] != -1:
            print([xx, yy])
surround([[-1, 0], [0, 0]], (1, 1))

def judge(A, target): # Q2: whether all of the 0 can arrive at target
    # time: O(mn) space: O(mn)
    if not A or A[target[0]][target[1]] == -1:
        return False
    m, n = len(A), len(A[0])
    starts = sum(A[i][j] == 0 for i in range(m) for j in range(n))
    dq = collections.deque([target])
    seen = {target}
    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            xx, yy = x + dx, y + dy
            if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen and A[xx][yy] != -1:
                seen.add((xx, yy))
                dq.append((xx, yy))
    return len(seen) == starts

if __name__ == '__main__':
    print(judge([[0],[0],[0]], (0,0))) # should print true
    print(judge([[0],[-1],[0]], (0,0))) # should print false


def shortestPathWithTreasures(A, start, end):
    if not A or A[start[0]][start[1]] == -1 or A[end[0]][end[1]] == -1:
        return -1
    m, n = len(A), len(A[0])
    treasures = sum(A[i][j] == 1 for i in range(m) for j in range(n))
    shortestPath = []

    def dfs(path, i, j, collected, seen):
        nonlocal shortestPath
        if i >= m or i < 0 or j >= n or j < 0 or A[i][j] == -1 or (i, j) in seen: return
        if A[i][j] == 1:
            collected.add((i, j))
        path.append((i, j))
        seen.add((i, j))
        if (i, j) == end:
            if len(collected) == treasures:
                if len(path) < len(shortestPath) or not shortestPath:
                    shortestPath = list(path)
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            dfs(path, i + di, j + dj, collected, seen)
        if A[i][j] == 1:
            collected.remove((i, j))
        path.pop()
        seen.remove((i, j))

    dfs([], start[0], start[1], set(), set())
    return shortestPath

print(shortestPathWithTreasures([[1,0,0],[1,1,0],[0,0,0],[1,1,1]], (0, 0), (2,2)))


# print(judge([[0, 0, 0], [0, 0, 0]], (1, 0)))
# print(judge([[0, -1, 0], [0, 0, 0]], (1, 0)))
# print(judge([[0, -1, 0], [0, 0, 0]], (0, 1)))

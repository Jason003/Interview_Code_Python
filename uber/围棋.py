import collections
def solution(A, point):
    if not A: return False
    x, y = point
    v = A[x][y]
    m, n = len(A), len(A[0])

    corner = 0

    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
        if x == 0 and y == 0 or x == m - 1 and y == 0 or x == 0 and y == n - 1 or x == m - 1 and y == n - 1:
            corner = 2
        else:
            corner = 1

    if v == '.': return False
    dq = collections.deque([(x, y)])
    seen = {(x, y)}

    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if not (0 <= xx < m and 0 <= yy < n):
                if not corner:
                    return False
                else:
                    corner -= 1
                    continue
            if (xx, yy) not in seen:
                seen.add((xx, yy))
                if A[xx][yy] == '.':
                    return False
                elif A[xx][yy] == v:
                    dq.append((xx, yy))
    return True


print(solution([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'X']], (2, 2)))

import collections
def solution(A, point):
    if not A: return False
    x, y = point
    v = A[x][y]
    m, n = len(A), len(A[0])

    def corner(x, y):
        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            xx, yy = x + dx, y + dy
            if 0 <= xx < m and 0 <= yy < n:
                if A[xx][yy] == '.' or A[xx][yy] == v:
                    return False
        return True
    if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and corner(x, y):
        return True

    if v == '.': return False
    dq = collections.deque([(x, y)])
    seen = {(x, y)}

    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if not (0 <= xx < m and 0 <= yy < n):
                return False
            if (xx, yy) not in seen:
                seen.add((xx, yy))
                if A[xx][yy] == '.':
                    return False
                elif A[xx][yy] == v:
                    dq.append((xx, yy))
    return True


print(solution([['X', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], (0, 0)))

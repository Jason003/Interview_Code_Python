from collections import deque


class Solution:
    def shortestDistance(self, grid):
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        cnt = 0
        distance = [[0 for i in range(n)] for i in range(m)]
        counts = [[0 for i in range(n)] for i in range(m)]
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    queue.append((i, j, 0))
                    marked = [[False for i in range(n)] for i in range(m)]
                    while queue:
                        cur_i, cur_j, dist = queue.popleft()
                        for direction in directions:
                            new_i = cur_i + direction[0]
                            new_j = cur_j + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0 and not marked[new_i][
                                new_j]:
                                counts[new_i][new_j] += 1
                                distance[new_i][new_j] += dist + 1
                                queue.append((new_i, new_j, dist + 1))
                                marked[new_i][new_j] = True
        for i in range(m):
            for j in range(n):
                if counts[i][j] == cnt and distance[i][j] < min_dist:
                    min_dist = distance[i][j]
        return min_dist if min_dist < float('inf') else -1

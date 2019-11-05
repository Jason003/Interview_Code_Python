class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n, all, dup = len(grid), len(grid[0]), 0, 0

        def count(i, j):
            return (grid[i - 1][j] if i > 0 else 0) + (grid[i + 1][j] if i < m - 1 else 0) + (
            grid[i][j - 1] if j > 0 else 0) + (grid[i][j + 1] if j < n - 1 else 0)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    all += grid[i][j]
                    dup += count(i, j)
        return all * 4 - dup

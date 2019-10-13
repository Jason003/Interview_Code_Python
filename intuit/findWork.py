def findWord(word, grid):
    # time complexity: O(m * n * 2 ^ len(word)), space complexity: O(len(word))
    if not grid:
        print('None')
        return

    def dfs(i, j, idx, route):
        if idx == len(word): return True
        if i >= m or j >= n or grid[i][j] != word[idx]:
            return False
        route.append((i, j))
        for di, dj in ((1, 0), (0, 1)):  # go to the below or right letter
            if dfs(i + di, j + dj, idx + 1, route): return True
        route.pop()
        return False

    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            route = []
            if dfs(i, j, 0, route):
                for x, y in route:
                    print(str(x) + ' ' + str(y))
                return
    print("None")


findWord('abcd', [['a', 'b', 'c', 'd'], ['b', 'c', 'e', ''], ['d', '', '', '']])
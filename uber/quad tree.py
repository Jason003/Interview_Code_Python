
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid):
    def dfs(r1, r2, c1, c2):
        if r1 > r2 or c1 > c2:
            return None
        val = grid[r1][c1]
        flag = True
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if grid[i][j] != val:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            return Node(val == 1, True, None, None, None, None)
        else:
            rm, cm = (r1 + r2) // 2, (c1 + c2) // 2
            return Node(True, False, dfs(r1, rm, c1, cm), dfs(r1, rm, cm + 1, c2), dfs(rm + 1, r2, c1, cm), dfs(rm + 1, r2, cm + 1, c2))
    n = len(grid)
    return dfs(0, n - 1, 0, n - 1)

def preorder(node):
    if not node:
        return
    print(str(node.val) + ' ' + str(node.isLeaf))
    preorder(node.topLeft)
    preorder(node.topRight)
    preorder(node.bottomLeft)
    preorder(node.bottomRight)

l = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
tree = construct(l)
preorder(tree)

'''
I think the time complexity is O(n^2 * log N) since we have log N^2 levels, and in each level we visit N^2 cells at most, where grid is N x N matrix.
'''
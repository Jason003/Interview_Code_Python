# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, node, parent):
            if not node:
                return
            if parent and node and parent.val + 1 == node.val:
                curr += 1
            else:
                curr = 1
            self.res = max(self.res, curr)
            dfs(curr, node.left, node)
            dfs(curr, node.right, node)

        dfs(0, root, None)
        return self.res

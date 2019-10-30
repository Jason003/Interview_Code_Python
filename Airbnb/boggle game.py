class Node:
    def __init__(self):
        self.word, self.children = None, {}


class Solution:
    def findWords(self, A, words):
        if not A:
            return []

        # build trie
        root = Node()
        for w in set(words):
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.word = w

        m, n = len(A), len(A[0])

        self.max = 0 # maximum words that can exist on the board at the same time
        res = []

        def dfs(i, j, curr):
            if i < 0 or i >= m or j < 0 or j >= n or A[i][j] not in curr.children:
                return

            curr = curr.children[A[i][j]]
            c = A[i][j]
            A[i][j] = '#'

            if curr.word:
                res.append(curr.word)
                self.max = max(self.max, len(res))
                for i in range(m):
                    for j in range(n):
                        dfs(i, j, root)
                A[i][j] = c
                res.pop()
                return

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + di, j + dj, curr)
            A[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return self.max

A = [["o","a","t","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

print(Solution().findWords(A, words))
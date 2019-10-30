import collections


def minimumVertexToTraverse(edges):
    graph = collections.defaultdict(set)
    for s, e in edges:
        graph[s].add(e)

    visited = set()
    res = set()

    def dfs(curr, start):
        if curr in temp:
            return
        temp.add(curr)
        if curr in res and curr != start:
            res.remove(curr)
            return
        for nxt in graph[curr]:
            dfs(nxt, start)

    for curr in graph:
        if curr not in visited:
            res.add(curr)
            temp = set()
            dfs(curr, curr)
            visited |= temp
    return res


edge1 = [[0, 0], [1, 2], [2, 0], [2, 3], [3, 1]]
edge2 = [[0, 1], [1, 0], [2, 1], [2, 3], [3, 2], [4, 1]]
edge3 = [[0, 1], [1, 0], [2, 1], [3, 1], [3, 2]]
edge4 = [[2, 9], [3, 3], [3, 5], [3, 7], [4, 8], [5, 8], [6, 6], [7, 4], [8, 7], [9, 3], [9, 6]]
print(minimumVertexToTraverse(edge1))
print(minimumVertexToTraverse(edge2))
print(minimumVertexToTraverse(edge3))
print(minimumVertexToTraverse(edge4))
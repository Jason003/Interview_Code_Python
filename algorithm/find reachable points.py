def findReachablePoints(graph):
    n = len(graph)

    parent = {i : i for i in range(n)} # parent for each node

    # union find
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for i in range(n):
        for neighbor in graph[i]:
            union(i, neighbor)

    result = []

    for i in range(n):
        reachablePoints = []
        for p in parent:
            if parent[p] == parent[i]:
                reachablePoints.append(p)
        result.append(reachablePoints)

    return result

print(findReachablePoints([[1],[2],[]]))
import collections
def costOfNodes(A):
    d = collections.defaultdict(set)
    for a in A:
        for i in range(1, len(a)):
            d[a[i]].add(a[0])
        d[a[0]].add(a[0])

    def dfs(a, seen):
        if a in seen:
            return
        seen.add(a)
        for neighbor in d[a]:
            dfs(neighbor, seen)

    res = []
    for k in set(d.keys()):
        seen = set()
        dfs(k, seen)
        res.append((k, len(seen)))
    return res

print(costOfNodes([['A', 'E', 'N', 'S'], ['S', 'H', 'N'], ['E', 'N'], ['H'], ['N']]))



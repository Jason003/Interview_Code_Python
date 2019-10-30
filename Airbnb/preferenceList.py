import collections
def preferenceList(A):
    prev = collections.defaultdict(set)
    after = collections.defaultdict(set)
    allList = set()
    for a in A:
        for i in range(len(a) - 1):
            pre, nxt = a[i], a[i + 1]
            prev[nxt].add(pre)
            after[pre].add(nxt)
            allList.add(pre)
            allList.add(nxt)
    res = set()
    def dfs(curr, currList, seen):
        if len(currList) == len(allList):
            res.add(tuple(currList))
            return
        if prev[curr] or curr in seen:
            return
        for nxt in after[curr]:
            prev[nxt].discard(curr)
        for nxt in allList - seen:
            dfs(nxt, currList + [curr], seen | {curr})
        for nxt in after[curr]:
            prev[nxt].add(curr)

    for i in allList:
        dfs(i, [], set())
    return res

print(preferenceList([[2,3,5], [4,2,1], [4,1,5,6], [4,7]]))


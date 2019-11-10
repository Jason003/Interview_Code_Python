import collections


# DFS solution.
def preferenceList_dfs(A):
    visited = {}
    graph = collections.defaultdict(set)
    for a in A:
        for i, c in enumerate(a):
            visited[c] = False
            if i < len(a) - 1:
                graph[a[i]].add(a[i + 1])

    def valid(ancestors, curr):
        if curr in ancestors:
            return False # invalid, there is a circle
        if visited[curr]:
            return True
        visited[curr] = True
        for nxt in graph[curr]:
            if not valid(ancestors | {curr}, nxt):
                return False
        res.append(curr) # add the one which has no prior character
        return True

    res = []
    for p in visited:
        if not valid(set(), p):
            return ''
    return res[::-1]

# print(preferenceList_dfs([[2,3,5], [4,2,1], [4,1,5,6], [4,7]]))

# toposort
def preferenceList_toposort(A):
    pre = collections.defaultdict(set)  # {character A : characters that is in front of A}
    is_pre = collections.defaultdict(set)  # {character A : characters that is in front of A}
    whole = set()
    # get relations between characters using words list
    for a in A:
        for i in range(len(a) - 1):
            pre[a[i + 1]].add(a[i])
            is_pre[a[i]].add(a[i + 1])
            whole.add(a[i + 1])
            whole.add(a[i])

    dq = collections.deque([c for c in whole if not pre[c]])
    res = []
    while dq:
        curr = dq.popleft()
        res.append(curr)
        for after in is_pre[curr]:
            pre[after].discard(curr)
            if not pre[after]:
                dq.append(after)
    return res if len(res) == len(whole) else []

# print all
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

print(preferenceList_toposort([[2,3,5], [4,2,1], [4,1,5,6], [4,7]]))


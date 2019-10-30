import collections
import heapq
# bellman ford
def shortestPath_bellman_ford(times, N, S, D): # S is source, D is destination
    # bellman ford, O(VE)
    dp = [0] + [float('inf')] * N
    pathTo = {}
    dp[S] = 0
    for _ in range(N):
        for u, v, w in times:
            if dp[u] != float('inf') and dp[u] + w < dp[v]:
                dp[v] = dp[u] + w
                pathTo[v] = u
    path = []
    end = D
    while end != S:
        path.append(end)
        end = pathTo[end]
    path.append(S)
    path.reverse()
    print(path)
    return path, dp[D]

# dfs
def shortestPath_dfs(times, S, D):
    graph = collections.defaultdict(dict)
    for s, e, t in times:
        graph[s][e] = t
    path = {}
    mem = {}
    def dfs(curr):
        # O(VE + E)
        if curr == D:
            return 0
        if curr in mem:
            return mem[curr]
        res = float('inf')
        for neigh in graph[curr]:
            tep = graph[curr][neigh] + dfs(neigh)
            if tep < res:
                path[curr] = neigh
                res = tep
        mem[curr] = res
        return res
    res = dfs(S)
    path_arr = []
    start = S
    while start != D:
        path_arr.append(start)
        start = path[start]
    return res, path_arr + [D] if res != float('inf') else -1

# Dijkstra
def shortestPath_dijk(times, S, D):
    # O(VlogV + E)
    graph = collections.defaultdict(dict)
    for s, e, t in times:
        graph[s][e] = t
    path = {}
    heap = [(0, None, S)]
    seen = set()
    while heap:
        time, pre, curr = heapq.heappop(heap)
        if curr in seen:
            continue
        seen.add(curr)
        if pre:
            path[pre] = curr
        if curr == D:
            path_arr = []
            start = S
            while start != D:
                path_arr.append(start)
                start = path[start]
            return time, path_arr + [D]
        for neighbor in graph[curr]:
            if neighbor not in seen:
                heapq.heappush(heap, (time + graph[curr][neighbor], curr, neighbor))
    return -1

print(shortestPath_dijk([[1,2,3],[2,3,4],[3,4,5],[1,4,6]], 1, 4))
    

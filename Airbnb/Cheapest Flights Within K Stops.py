import collections
import heapq


class Solution:
    def findCheapestPrice(self, flights, src, dst, K):
        '''
        no cycle detection, because we can only move K steps, there will not be a circle problem
        '''
        graph = collections.defaultdict(dict)
        for s, e, cost in flights:
            graph[s][e] = cost
        heap = [(0, src, K + 1)]
        while heap:
            cost, curr, stops = heapq.heappop(heap)
            if curr == dst:
                return cost
            if stops:
                for nxt, price in graph[curr].items():
                    heapq.heappush(heap, (cost + price, nxt, stops - 1))
        return -1

    def findCheapestPrice_bellman(self, flights, src, dst, K, n):
        # bellman ford

        dp = [[float("inf")] * (K + 2) for _ in range(n)]
        dp[src] = [0] * (K + 2)
        for k in range(1, K + 2):
            for u, v, w in flights:
                if dp[u][k - 1] != float('inf') and dp[u][k - 1] + w < dp[v][k]: dp[v][k] = dp[u][k - 1] + w
        return dp[dst][K + 1] if dp[dst][K + 1] != float('inf') else -1

    def findCheapestPrice_bellman_1d(self, flights, src, dst, K, n):
        # bellman ford
        dp = [float("inf")] * n
        dp[src] = 0
        for k in range(K + 1):
            tep = dp[:]
            for u, v, w in flights:
                if dp[u] != float('inf') and dp[u] + w < tep[v]:
                    tep[v] = dp[u] + w
            dp = tep
        return dp[dst] if dp[dst] != float('inf') else -1

    def findCheapestPrice_optimized(self, flights, src, dst, K):
        '''
        used a dictionary to track the number of movies it took to reach a node,
        and then i only visit the node again if the current path took fewer moves
        to reach the node than any previous path.
        '''
        graph = collections.defaultdict(dict)
        for s, e, cost in flights:
            graph[s][e] = cost
        heap = [(0, src, 0)]
        seen = {}  # city : steps
        while heap:
            cost, curr, steps = heapq.heappop(heap)
            if curr == dst:
                return cost
            if curr in seen and seen[curr] < steps:  # if
                continue
            seen[curr] = steps
            if steps <= K:
                for nxt, price in graph[curr].items():
                    heapq.heappush(heap, (cost + price, nxt, steps + 1))
        return -1

    def findCheapestPrice_dfs(self, n, flights, src, dst, K):
        # dfs
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        self.res = float('inf')

        def dfs(curr, cost, k, seen):
            if k < 0 or cost >= self.res or curr in seen:
                return
            if curr == dst:
                self.res = min(self.res, cost)
                return
            for nxt, add_cost in graph[curr].items():
                dfs(nxt, cost + add_cost, k - 1, seen | {curr})

        dfs(src, 0, K + 1, set())
        return self.res if self.res != float('inf') else -1


def shortest_path(edges, src, dst, n):
    # bellman ford
    dp = [[float("inf")] * (n + 1) for _ in range(n)]
    dp[src] = [0] * (n + 1)
    for k in range(1, n + 1):
        for u, v, w in edges: # vertex u, vertex v and weight of edge (u, v)
            if dp[u][k - 1] != float('inf') and dp[u][k - 1] + w < dp[v][k]:
                dp[v][k] = dp[u][k - 1] + w
    return dp[dst][n]


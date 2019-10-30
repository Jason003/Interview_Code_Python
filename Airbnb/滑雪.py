import collections
import heapq


def solution_bfs(travel, point):
    '''
    :param travel: [[start, cost, end]] all strings
    :param point: [[end, rewards]] all strings
    :return: max reward, path
    '''
    # we need to find the minimum cost one
    point = {end: int(reward) for end, reward in point}
    graph = collections.defaultdict(dict)
    for start, cost, end in travel:
        graph[start][end] = int(cost) - point.get(end, 0)
    path = {}  # record path
    # dijkstra
    heap = [(0, 'start', None)]  # cost, current position, previous position
    seen = {}  # records the position and cost
    res = -float('inf')
    while heap:
        cost, curr, pre = heap.pop()
        if pre:
            path[pre] = curr
        if curr == 'end':
            res = max(-cost, res)
        if curr in seen and cost > seen[curr]:
            continue
        seen[curr] = cost
        for nxt, add_cost in graph[curr].items():
            heapq.heappush(heap, (cost + add_cost, nxt, curr))
    path_arr = []
    start = 'start'
    while start != 'end':
        path_arr.append(start)
        start = path[start]
    return (res, path_arr + ['end']) if res != -float('inf') else (-1, [])


#
# travel = [['start', '100', 'A'], ['A', '100', 'B'], ['B', '100', 'end'], ['start', '0', 'end']]
# point = [['A', '200'], ['B', '0'], ['end', '400']]
# print(solution_bfs(travel, point))

def solution_bellman_ford(travel, point):
    point = {end: int(reward) for end, reward in point}
    graph = collections.defaultdict(dict)
    for start, cost, end in travel:
        graph[start][end] = int(cost) - point.get(end, 0)
    path = {}  # record path
    cost = {}  # cost means the minimum cost to arrive at this position
    for s, c, e in travel:
        cost.setdefault(s, float('inf'))
        cost.setdefault(e, float('inf'))
    cost['start'] = 0
    for _ in cost:
        for i, v in graph.items():
            for j, add in v.items():
                if cost[i] != float('inf') and cost[i] + add < cost[j]:
                    cost[j] = cost[i] + add
                    path[i] = j
    if cost[end] == float('inf'):
        return -1
    path_arr = []
    start = 'start'
    while start != 'end':
        path_arr.append(start)
        start = path[start]
    return -cost[end], path_arr + ['end']


travel = [['start', '100', 'A'], ['A', '100', 'B'], ['B', '100', 'end'], ['start', '0', 'end']]
point = [['A', '200'], ['B', '0'], ['end', '400']]
print(solution_bellman_ford(travel, point))


def findMaxScore(paths, rewards, start):
    pathMap = collections.defaultdict(dict)
    rewardMap = collections.Counter()
    scoreMap = collections.Counter()  # help us to prune the branches

    for s, e, score in paths:
        pathMap[s][e] = int(score)

    for place, reward in rewards:
        rewardMap[place] += int(reward)

    ends = set()

    max_score = -float('inf')
    max_path = None

    for s, e, score in paths:
        if not pathMap[e]:
            ends.add(e)
            scoreMap[e] = 0

    def dfs(currPath, curr, score):
        nonlocal max_score, max_path
        currPath.append(curr)
        if curr in ends:
            if score > max_score:
                max_score = score
                max_path = list(currPath)
            currPath.pop()
            return
        for nxt in pathMap[curr]:
            newScore = score + 2 * rewardMap[nxt] + pathMap[curr][nxt]
            if newScore <= scoreMap[nxt]:
                continue
            scoreMap[nxt] = newScore
            dfs(currPath, nxt, newScore)
        currPath.pop()

    dfs([], start, 2 * rewardMap[start])
    return max_score, max_path


print(findMaxScore(
    [['A', 'B', '2'], ['A', 'C', '3'], ['B', 'D', '5'], ['B', 'E', '6'], ['C', 'E', '4'], ['C', 'F', '4'],
     ['D', 'H', '7'],
     ['E', 'H', '6'],
     ['H', 'I', '1'],
     ['H', 'J', '2'], ['F', 'J', '3']],
    [['A', '5'], ['B', '7'], ['C', '6'], ['D', '2'], ['E', '4'], ['F', '7'], ['H', '7'], ['I', '3'], ['J', '2']], 'A'))

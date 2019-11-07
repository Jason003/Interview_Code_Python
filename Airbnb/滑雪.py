import collections
import heapq

# 多个终点，路径消耗reward
def ski_bfs(travel, reward, src):
    reward_map = {end : int(points) for end, points in reward}
    graph = collections.defaultdict(dict)
    for start, end, cost in travel:
        graph[start][end] = int(cost)
    path = {} # record path
    ends = {end for start, end, cost in travel if end not in graph} # end points
    dq = collections.deque([(src, reward_map[src], None)])
    score_map = {}
    maxEnd = None
    while dq:
        curr_location, curr_score, pre = dq.popleft()
        if curr_location not in score_map or curr_score > score_map[curr_location]:
            score_map[curr_location] = curr_score
            if pre:
                path[curr_location] = pre

        if curr_location in ends:
            if not maxEnd or score_map[curr_location] > score_map[maxEnd]:
                maxEnd = curr_location

        for nxt_location, cost in graph[curr_location].items():
            dq.append((nxt_location, curr_score - cost + reward_map[nxt_location], curr_location))

    path_arr = []
    temp = maxEnd
    while temp in path:
        path_arr.append(temp)
        temp = path[temp]
    path_arr.append(src)
    return (score_map[maxEnd], path_arr[::-1]) if maxEnd else (None, None)

def ski_dfs(paths, rewards, start):
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
            newScore = score + rewardMap[nxt] - pathMap[curr][nxt]
            if newScore <= scoreMap[nxt]:
                continue
            scoreMap[nxt] = newScore
            dfs(currPath, nxt, newScore)
        currPath.pop()

    dfs([], start, rewardMap[start])
    return max_score, max_path

# 给了终点
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
        tep = dict(cost)
        for i, v in graph.items():
            for j, add in v.items():
                if cost[i] != float('inf') and cost[i] + add < tep[j]:
                    tep[j] = cost[i] + add
                    path[i] = j
        cost = tep
    if cost['end'] == float('inf'):
        return -1
    path_arr = []
    start = 'start'
    while start != 'end':
        path_arr.append(start)
        start = path[start]
    return -cost['end'], path_arr + ['end']


# travel = [['start', '100', 'A'], ['A', '100', 'B'], ['B', '100', 'end'], ['start', '0', 'end']]
# point = [['A', '200'], ['B', '0'], ['end', '400']]
# print(solution_bellman_ford(travel, point))





print(ski_dfs(
    [['A', 'B', '2'], ['A', 'C', '3'], ['B', 'D', '5'], ['B', 'E', '6'], ['C', 'E', '4'], ['C', 'F', '4'],
     ['D', 'H', '7'],
     ['E', 'H', '6'],
     ['H', 'I', '1'],
     ['H', 'J', '2'], ['F', 'J', '3']],
    [['A', '5'], ['B', '7'], ['C', '6'], ['D', '2'], ['E', '4'], ['F', '7'], ['H', '7'], ['I', '3'], ['J', '2']], 'A'))
print(ski_bfs(
    [['A', 'B', '2'], ['A', 'C', '3'], ['B', 'D', '5'], ['B', 'E', '6'], ['C', 'E', '4'], ['C', 'F', '4'],
     ['D', 'H', '7'],
     ['E', 'H', '6'],
     ['H', 'I', '1'],
     ['H', 'J', '2'], ['F', 'J', '3']],
    [['A', '5'], ['B', '7'], ['C', '6'], ['D', '2'], ['E', '4'], ['F', '7'], ['H', '7'], ['I', '3'], ['J', '2']], 'A'))
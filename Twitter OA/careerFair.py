def solution(arrival, duration):
    events = [(i, i + j) for i, j in zip(arrival, duration)]
    events.sort(key = lambda x : x[1])
    res = 0
    end = -1
    for s, e in events:
        if s >= end:
            res += 1
            end = e
    return res

print(solution([1,3,3,5,7], [2,2,1,2,1]))
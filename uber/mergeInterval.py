def mergeInterval(A):
    A.sort()
    res = []
    for s, e in A:
        if not res or s > res[-1][1]:
            res.append([s, e])
        else:
            res[-1][1] = max(res[-1][1], e)
    return res


'''
如果给一个list of interval，already sorted but not merged yet, 和一个还没来得及merge的单独的interval，如何merge整个list和这个单独的interval in one pass
'''

def merge_into_sorted_intervals(intervals, interval):

    def add(intervals, interval):
        if not intervals or interval[0] > intervals[-1][1]:
            intervals.append(interval)
        else:
            intervals[-1][1] = max(intervals[-1][1], interval[1])

    left, right = [], []
    for s, e in intervals:
        if e < interval[0]:
            add(left, [s, e])
        elif s > interval[1]:
            add(right, [s, e])
        else:
            interval[0] = min(interval[0], s)
            interval[1] = max(interval[1], e)

    return left + [interval] + right

print(merge_into_sorted_intervals([[1,5],[2,5],[3,4],[5,6]], [20,30]))
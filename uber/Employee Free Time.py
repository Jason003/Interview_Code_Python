class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution1:
    def employeeFreeTime(self, schedule):
        intervals = []
        for i in schedule:
            intervals += i
        merged = []
        for i in sorted(intervals, key = lambda x: (x.start, x.end)):
            s, e = i.start, i.end
            if not merged:
                merged.append(i)
            elif s <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, e)
            else:
                merged.append(i)
        freeTime = []
        if not merged: return []
        for i in range(len(merged) - 1):
            freeTime.append(Interval(merged[i].end, merged[i + 1].start))
        return freeTime

class Solution2: # 扫描线
    def employeeFreeTime(self, schedule):
        timeStamp = []
        for sch in schedule:
            for interval in sch:
                timeStamp.append((interval[0], 0))
                timeStamp.append((interval[1], 1))
        timeStamp.sort()
        res = []
        start = -1
        cnt = 0
        for time, status in timeStamp:
            if status == 0: # start
                if cnt == 0 and start != -1:
                    res.append((start, time))
                cnt += 1
            else: # end
                cnt -= 1
                if cnt == 0:
                    start = time
        return res

    # follow up: if we need find free time that >= k people are in rest
    def moreThanKFreeWorkers(self, schedule, k):
        timeStamp = []
        for sch in schedule:
            for interval in sch:
                timeStamp.append((interval.start, 0))
                timeStamp.append((interval.end, 1))
        timeStamp.sort()
        res = []
        start = -1
        totalWorkers = len(schedule)
        numAtWork = 0
        for time, status in timeStamp:
            if status == 0:  # start
                if numAtWork == totalWorkers - k and start != -1:
                    res.append(Interval(start, time))
                numAtWork += 1
            else:  # end
                numAtWork -= 1
                if numAtWork == totalWorkers - k:
                    start = time
        return res

A = [[[1,4], [7,11], [15,19]], [[4 ,6], [8,9], [11,13], [20,29]], [[4,10], [25,35]]]
print(Solution2().employeeFreeTime(A))
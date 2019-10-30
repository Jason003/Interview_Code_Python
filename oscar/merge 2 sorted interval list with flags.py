
# Definition of Interval.
class Interval(object):
    def __init__(self, start, end, flag):
        self.start = start
        self.end = end
        self.flag = flag



class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        i, j = 0, 0
        intervals = []
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(intervals, list1[i])
                i += 1
            else:
                self.push_back(intervals, list2[j])
                j += 1
        while i < len(list1):
            self.push_back(intervals, list1[i])
            i += 1
        while j < len(list2):
            self.push_back(intervals, list2[j])
            j += 1

        return intervals

    def push_back(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return

        last_interval = intervals[-1]
        if last_interval.end < interval.start:
            intervals.append(interval)
            return
        if last_interval.flag == interval.flag:
            intervals[-1].end = max(interval.end, intervals[-1].end)
        else:
            intervals[-1].end = 
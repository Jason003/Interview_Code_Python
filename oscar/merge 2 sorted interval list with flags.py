
# Definition of Interval.
class Interval(object):
    def __init__(self, start, end, flag):
        self.start = start
        self.end = end
        self.flag = flag
    def __str__(self):
        return str(self.start) + ',' + str(self.end) + ',' + str(self.flag)


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

        last_interval = Interval(intervals[-1].start, intervals[-1].end, intervals[-1].flag)
        if last_interval.end <= interval.start:
            intervals.append(interval)
            return

        if last_interval.end <= interval.end:
            if intervals[-1].start < interval.start:
                intervals[-1].end = interval.start
            else:
                intervals.pop()
            if interval.start < last_interval.end:
                intervals.append(Interval(interval.start, last_interval.end, interval.flag and last_interval.flag))
            if last_interval.end != interval.end:
                intervals.append(Interval(last_interval.end, interval.end, interval.flag))
        else:
            intervals[-1].end = interval.start
            intervals.append(interval)
            intervals[-1].flag = last_interval.flag and interval.flag
            intervals.append(Interval(interval.end, last_interval.end, last_interval.flag))

sol = Solution()
for i in sol.mergeTwoInterval([Interval(2,5,True)], [Interval(1, 4, False), Interval(4, 8, True)]):
    print(i)
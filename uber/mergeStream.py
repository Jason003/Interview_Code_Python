import collections, heapq
class Stream:
    def __init__(self, A):
        self.dq = collections.deque(A)

    def hasNext(self):
        return len(self.dq) > 0

    def next(self):
        if self.hasNext():
            return self.dq.popleft()

class MergedIterator:
    def __init__(self, streamList):
        self.heap = []
        self.idx = 0
        for stream in streamList:
            if stream.hasNext():
                heapq.heappush(self.heap, (stream.next(), self.idx, stream))
                self.idx += 1

    def hasNext(self):
        if not self.heap:
            return False
        return True

    def next(self):
        if self.hasNext():
            num, idx, stream = heapq.heappop(self.heap)
            if stream.hasNext():
                heapq.heappush(self.heap, (stream.next(), self.idx, stream))
                self.idx += 1
            return num

mergedIterator = MergedIterator([Stream([1,2,3,4,5]), Stream([3,10,11,20,57]), Stream([3,4,5,6,7])])

while mergedIterator.hasNext():
    print(mergedIterator.next())

import collections
class MyIterator:
    def __init__(self, A):
        self.dq = collections.deque(A)

    def next(self):
        if self.hasNext():
            return self.dq.popleft()
        return None

    def hasNext(self):
        while self.dq and type(self.dq[0]) == list:
            for i in self.dq.popleft()[::-1]:
                self.dq.appendleft(i)
        return len(self.dq) > 0

it = MyIterator([[[1,2,3,4]],[5,[6,7,8,4,3]], 7,5,2,4,[3,4,4]])
while it.hasNext():
    print(it.next())
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

# it = MyIterator([[[1, 2, 3, 4]], [5, [6, 7, 8, 4, 3]], 7, 5, 2, 4, [3, 4, 4]])
# while it.hasNext():
#     print(it.next())


class TwoDIterator:
    def __init__(self, A):
        self.A = A
        self.row = 0
        self.col = 0
        self.canRemove = False

    def next(self):
        if not self.hasNext():
            raise RuntimeError
        val = self.A[self.row][self.col]
        self.col += 1
        self.canRemove = True
        return val

    def hasNext(self):
        if not self.A:
            return False
        while self.row < len(self.A):
            if self.col < len(self.A[self.row]):
                return True
            else:
                self.row += 1
                self.col = 0
        return False

    def remove(self):
        if not self.canRemove:
            raise RuntimeError
        rowToBeRemoved = self.row
        colToBeRemoved = self.col
        if colToBeRemoved == 0:
            rowToBeRemoved -= 1
            colToBeRemoved = len(self.A[rowToBeRemoved]) - 1
        else:
            colToBeRemoved -= 1
        self.A[rowToBeRemoved].pop(colToBeRemoved)
        if not self.A[rowToBeRemoved]:
            del self.A[rowToBeRemoved]
        if self.col > 0:
            self.col -= 1
        self.canRemove = False


it = TwoDIterator([[1, 2], [3, 4], [5, 6]])
it.next()
it.remove()
it.next()
it.remove()
print(it.A)
print(it.next())
print(it.next())
print(it.next())

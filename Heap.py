class Heap:
    def __init__(self):
        self.A = []  # array store numbers
        self.N = 0  # current size

    def _swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def _swim(self, i):  # swim a key from lower to right place
        while (i - 1) // 2 >= 0:
            p = (i - 1) // 2
            if self.A[p] < self.A[i]:
                self._swap(p, i)
            else: break
            i = p

    def push(self, num):  # insert a new number to the heap
        self.A.append(num)
        self._swim(self.N)
        self.N += 1

    def _sink(self, i): # sink the key from higher to right place
        while i * 2 + 1 < self.N:
            c = i * 2 + 1
            if c + 1 < self.N and self.A[c] < self.A[c + 1]:  c += 1
            if self.A[c] > self.A[i]:
                self._swap(c, i)
            else: break
            i = c

    def pop(self):
        if self.N:
            self.N -= 1
            res = self.A[0]
            self._swap(0, self.N)
            self._sink(0)
            return res
import random
if __name__ == '__main__':
    heap = Heap()
    for i in range(100):
        heap.push(random.randint(1, 100))
    for j in range(100):
        print(heap.pop())
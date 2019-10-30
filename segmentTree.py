# use Segment Tree to deal with minimum number in a range
import unittest
import math
import random
class Solution:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.size = 1 << math.ceil(math.log(self.n, 2)) + 1
        self.tree = [None] * self.size
        self._build(0, 0, self.n - 1)

    def _build(self, pos, l, r):
        if l == r:
            self.tree[pos] = self.arr[l]
            return
        m = (l + r) // 2
        self._build(pos * 2 + 1, l, m)
        self._build(pos * 2 + 2, m + 1, r)
        self.tree[pos] = min(self.tree[pos * 2 + 1], self.tree[pos * 2 + 2])

    def _query(self, start, end, l, r, pos):
        if start > r or end < l: return float('inf')
        if start <= l and r <= end: return self.tree[pos]
        m = (l + r) // 2
        a = self._query(start, end, l, m, pos * 2 + 1)
        b = self._query(start, end, m + 1, r, pos * 2 + 2)
        return min(a, b)

    def query(self, start, end):
        res = self._query(start, end, 0, self.n - 1, 0)
        return res if res != float('inf') else -1

class Test(unittest.TestCase):
    def test_query(self):
        arr = [random.randint(1, 10000) for _ in range(100)]
        sol = Solution(arr)
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                self.assertEqual(sol.query(i, j), min(arr[i:j+1]))

if __name__ == '__main__':
    unittest.main()
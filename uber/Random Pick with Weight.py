import random, bisect


class Solution:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.n = len(w)
        self.a = [0] * (self.n + 1)
        for i in range(self.n):
            self.a[i + 1] = self.a[i] + w[i]
        self.max = self.a[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        idx = random.randint(0, self.max - 1)
        return bisect.bisect(self.a, idx) - 1

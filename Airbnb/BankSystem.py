import collections
class BankSystem:
    def __init__(self):
        self.acounts = collections.defaultdict(lambda : [(0, 0)])

    def deposit(self, id, amount, timestamp):
        self.acounts[id].append((timestamp, amount + self.acounts[id][-1][1]))

    def withdraw(self, id, amount, timestamp):
        if self.acounts[id][-1][1] < amount:
            return False
        self.acounts[id].append((timestamp, self.acounts[id][-1][1] - amount))
        return True

    def check(self, id, startTime, endTime):
        if id not in self.acounts:
            return
        # idx1 = bisect.bisect_left(self.acounts[id], (startTime + 1, )) - 1
        # idx2 = bisect.bisect_left(self.acounts[id], (endTime + 1, )) - 1
        idx1 = self._search(self.acounts[id], (startTime + 1, )) - 1
        idx2 = self._search(self.acounts[id], (endTime + 1, )) - 1
        return self.acounts[id][idx2][1] - self.acounts[id][idx1][1]

    def _search(self, A, k): # find the largest index i where A[i]
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if A[mi] == k:
                return mi
            elif A[mi] < k:
                lo = mi + 1
            else:
                hi = mi - 1
        return lo


backSystem = BankSystem()
backSystem.deposit(1,5,1000)
backSystem.deposit(1,3,2000)
backSystem.deposit(1,2,3000)
print(backSystem.check(1, 0, 1500))
print(backSystem.check(1, 1000, 2000))
print(backSystem.check(1, 0, 100000))
print(backSystem.check(1, 1000, 3000))
print(backSystem.check(1, 0, 3000))
print(backSystem.check(1, 4000, 5000))


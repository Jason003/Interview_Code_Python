class Solution:
	def __init__(self):
		self.A = []
		self.mul = []
	def insert(self, n):
		self.A.append(n)
		if not self.mul: self.mul.append(n)
		else: self.mul.append(self.mul[-1] * n)
	def getMul(self, k):
		if k > len(self.A): return None
		return self.mul[-1] // self.mul[-k - 1]

sol = Solution()
sol.insert(8)
sol.insert(2)
sol.insert(3)
sol.insert(4)
print(sol.getMul(3))
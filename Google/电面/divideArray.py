import collections

def judge(A):
	if not A: return False
	cnt = collections.Counter(A)
	return all(v >= 2 for v in cnt.values())

print(judge([1,1,1,3,3,4,4]))
print(judge([1,1,1,8,3,3,4,4]))
print(judge([]))
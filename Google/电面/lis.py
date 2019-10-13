import bisect

def lis(A):
	res = []
	for c in A:
		if not res:
			res.append(c)
		else:
			idx = bisect.bisect_left(res, c)
			if idx == len(res):
				res.append(c)
			else:
				res[idx] = c
	return len(res)

print(lis([3, 10, 2, 1, 20]))
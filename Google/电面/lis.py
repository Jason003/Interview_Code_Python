import bisect

# def lis(A):
# 	res = []
# 	for c in A:
# 		if not res:
# 			res.append(c)
# 		else:
# 			idx = bisect.bisect_left(res, c)
# 			if idx == len(res):
# 				res.append(c)
# 			else:
# 				res[idx] = c
# 	return len(res)

def lis(A):
	n = len(A)
	dp = [1] * n
	res = 0
	pre = [-1] * n
	idx = 0
	for i in range(n):
		for j in range(i):
			if A[i] > A[j] and dp[j] + 1 > dp[i]:
				dp[i] = dp[j] + 1
				pre[i] = j
		if dp[i] > res:
			res = dp[i]
			idx = i
	arr = []
	while idx != -1:
		arr.append(A[idx])
		idx = pre[idx]
	return arr[::-1]



print(lis([3, 10, 2, 1, 20]))
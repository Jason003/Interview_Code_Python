def shortestDistance(A, x, y):
	if x == y: return 0
	if x not in A or y not in A: return -1
	px, py = [], [] # positions of x and positions of y
	for i, a in enumerate(A):
		if a == x: px.append(i)
		elif a == y: py.append(i)
	res = float('inf') # shortest distance we should return
	i, j = 0, 0
	while i < len(px) and j < len(py):
		res = min(res, abs(px[i] - py[j]))
		if px[i] < py[j]: i += 1
		else: j += 1
	return res



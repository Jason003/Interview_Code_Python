import random
import time
def maxSubarray(A):
	res = 0 # max sum we should return
	curr = 0
	for a in A:
		curr = max(curr + a, a)
		res = max(res, curr)
	return res

def maxArrayButeForce(A):
    res = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            res = max(res, sum(A[i : j]))
    return res

start = time.time()
for _ in range(100):
    A = []
    for _ in range(100):
        A.append(random.randint(-100, 100))
        maxSubarray(A)
end = time.time()
print(end - start)

print('===========')

start = time.time()
for _ in range(100):
    A = []
    for _ in range(100):
        A.append(random.randint(-100, 100))
        maxArrayButeForce(A)
end = time.time()
print(end - start)
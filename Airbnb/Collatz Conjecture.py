def collatzConjecture(n): # iterative
    mx = 0
    seen = {}
    num = -1
    for i in range(1, n + 1):
        steps = 0
        curr = i
        while curr != 1:
            if curr in seen:
                steps += seen[curr]
                break
            if curr % 2:
                curr = curr * 3 + 1
            else:
                curr //= 2
            steps += 1
        seen[i] = steps
        if steps > mx:
            mx = steps
            num = i
    return mx, num

def collatzConjecture2(n): # recursive
    mx = 0
    seen = {}
    num = -1
    def helper(x):
        nonlocal mx, num
        if x == 1:
            return 0
        if x in seen:
            return seen[x]
        seen[x] = 1 + helper(x // 2 if x % 2 == 0 else 3 * x + 1)
        if seen[x] > mx:
            mx = seen[x]
            num = x
        return seen[x]
    for i in range(1, n + 1):
        helper(i)
    return mx, num


for n in range(1, 1000):
    assert collatzConjecture(n) == collatzConjecture2(n)
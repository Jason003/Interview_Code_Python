'''
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.
'''

def pourWater(A, V, K):

    def printWater():
        m, n = max(A), len(A)
        res = [[' '] * n for _ in range(m)]
        for j in range(n):
            for i in range(A[j]):
                res[-i-1][j] = 'w'
            for i in range(tep[j]):
                res[-i - 1][j] = '#'

        for row in res:
            print(''.join(row))
        print('============')

    tep = A[:]
    printWater()

    n = len(A)
    for _ in range(V):
        idx = K
        for i in range(K, -1, -1):
            if A[i] < A[idx]:
                idx = i
            elif A[i] > A[idx]:
                break
        if idx != K:
            A[idx] += 1
        else:
            for i in range(K, n):
                if A[i] < A[idx]:
                    idx = i
                elif A[i] > A[idx]:
                    break
            A[idx] += 1
        printWater()
    return A

pourWater([2,1,1,2,1,2,2], 15, 3)

# 左边有墙
def pourWater1(A, V, K):

    def printWater():
        m, n = max(A), len(A)
        res = [[' '] * n for _ in range(m)]
        for j in range(n):
            for i in range(A[j]):
                res[-i-1][j] = 'w'
        for j in range(K - preK, K - preK + len(tep)):
            for i in range(tep[j - K + preK]):
                res[-i-1][j] = '#'

        for row in res:
            print(''.join(row))
        print('============')
    preK = K
    tep = A[:]
    printWater()
    for _ in range(V):
        idx = K
        i = K
        while i >= 0:
            if A[i] < A[idx]:
                idx = i
            elif A[i] > A[idx]:
                break
            i -= 1
        if idx != K and i != -1:
            A[idx] += 1
        else:
            i = K
            while i < len(A):
                if A[i] < A[idx]:
                    idx = i
                elif A[i] > A[idx]:
                    break
                i += 1
            if i == len(A):
                continue
            A[idx] += 1
    printWater()
    return A

# 右边有墙
def pourWater2(A, V, K):

    def printWater():
        m, n = max(A), len(A)
        res = [[' '] * n for _ in range(m)]
        for j in range(n):
            for i in range(A[j]):
                res[-i-1][j] = 'w'
        for j in range(K - preK, K - preK + len(tep)):
            for i in range(tep[j - K + preK]):
                res[-i-1][j] = '#'

        for row in res:
            print(''.join(row))
        print('============')
    preK = K
    tep = A[:]
    printWater()
    for _ in range(V):
        idx = K
        i = K
        while i >= 0:
            if A[i] < A[idx]:
                idx = i
            elif A[i] > A[idx]:
                break
            i -= 1
        if i == -1:
            continue
        if idx != K:
            A[idx] += 1
        else:
            i = K
            while i < len(A):
                if A[i] < A[idx]:
                    idx = i
                elif A[i] > A[idx]:
                    break
                i += 1
            if i == len(A):
                A[K] += 1
                continue
            A[idx] += 1
    printWater()
    return A


# 两边都没有墙
def pourWater4(A, V, K): # no walls

    def printWater():
        m, n = max(A), len(A)
        res = [[' '] * n for _ in range(m)]
        for j in range(n):
            for i in range(A[j]):
                res[-i-1][j] = 'w'
        for j in range(K - preK, K - preK + len(tep)):
            for i in range(tep[j - K + preK]):
                res[-i-1][j] = '#'

        for row in res:
            print(''.join(row))
        print('============')
    preK = K
    tep = A[:]
    printWater()
    for _ in range(V):
        idx = K
        i = K
        while i >= 0:
            if A[i] < A[idx]:
                idx = i
            elif A[i] > A[idx]:
                break
            i -= 1
        if i == -1:
            continue
        if idx != K:
            A[idx] += 1
        else:
            i = K
            while i < len(A):
                if A[i] < A[idx]:
                    idx = i
                elif A[i] > A[idx]:
                    break
                i += 1
            if i == len(A):
                continue
            A[idx] += 1
    printWater()
    return A

# 两边都有墙，不是先左后右，而是哪个最低去哪个
def pourWater5(A, V, K):

    def printWater():
        m, n = max(A), len(A)
        res = [[' '] * n for _ in range(m)]
        for j in range(n):
            for i in range(A[j]):
                res[-i-1][j] = 'w'
            for i in range(tep[j]):
                res[-i - 1][j] = '#'

        for row in res:
            print(''.join(row))
        print('============')

    tep = A[:]
    printWater()

    n = len(A)
    for _ in range(V):
        idxLeft, idxRight = K, K
        for i in range(K, -1, -1):
            if A[i] < A[idxLeft]:
                idxLeft = i
            elif A[i] > A[idxLeft]:
                break
        for i in range(K, n):
            if A[i] < A[idxRight]:
                idxRight = i
            elif A[i] > A[idxRight]:
                break
        if A[idxLeft] < A[idxRight]:
            A[idxLeft] += 1
        else:
            A[idxRight] += 1
        printWater()
    return A

# pourWater5([5,4,3,2,5], 10, 2)

'''
BFS，用一个set存遍历到locked但是还没有key来开锁的box，每次获得key的时候就去找这个set里面有没有可以被打开的box

input：Box start
output：int candies

box类含有的信息如下：
Box A
A is unlocked
A has 2 candies
A contains box B
A has a key to B

Box B
B is locked
B has 2 candies
B contains no box
B has no keys

输入会给一个Box，题目要求的是一直到你无法打开任意一个Box为止，最多能拿到多少candies
'''
class Box:
    def __init__(self, locked, candies, innerBoxes, keys, name):
        self.locked = locked
        self.candies = candies
        self.innerBoxes = innerBoxes
        self.keys = keys
        self.name = name

import collections
def box_and_candy(box):
    dq = collections.deque([box])
    res = 0
    unlockedBoxes = {}
    while dq:
        curr = dq.popleft()
        if curr.locked: continue
        res += curr.candies
        for innerBox in curr.innerBoxes:
            if innerBox.locked:
                unlockedBoxes[innerBox.name] = innerBox
            else:
                dq.append(innerBox)
        for key in curr.keys:
            if key in unlockedBoxes:
                box = unlockedBoxes[key]
                unlockedBoxes.pop(key)
                box.locked = False
                dq.append(box)
    return res

b = Box(True, 2, [], [], 'b')
a = Box(False, 2, [b], ['b'], 'a')
print(box_and_candy(b))



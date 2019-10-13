def canChangeWith1(A, user):
    if user not in A or not A[user]:
        return False
    target = A[user][0]
    if target not in A or not A[target]:
        return False
    return A[target][0] == user

def canChange(A, user, rank):
    if user not in A or len(A[user]) <= rank:
        return False
    target = A[user][rank]
    if target not in A or len(A[target]) <= rank:
        return False
    return A[target][rank] == user

def changeRank(A, user, rank):
    def judge():
        res = set()
        for user in A:
            for i in range(len(A[user])):
                if canChange(A, user, i):
                    res.add(user)
                    break
        return res
    pre = judge()
    A[user][rank], A[user][rank - 1] = A[user][rank - 1], A[user][rank]
    after = judge()
    return after - pre

# print(changeRank({'a':['b','c'], 'b':['a','c'], 'c':['a', 'b', 'd'], 'd':['e', 'c', 'f']}, 'd', 2))

import unittest

class Test(unittest.TestCase):

    def test_canChangeWith1(self):
        self.assertEqual(canChangeWith1({'a':['b','c'], 'b':['a','c'], 'c':['b', 'a']}, 'a'), True)
        self.assertEqual(canChangeWith1({'a':['b','c'], 'b':['a','c'], 'c':['b', 'a']}, 'c'), False)


    def test_canChange(self):
        self.assertEqual(canChange({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'a']}, 'a', 0), True)
        self.assertEqual(canChange({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'a']}, 'a', 1), True)
        self.assertEqual(canChange({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'a']}, 'c', 0), False)
        self.assertEqual(canChange({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'a']}, 'c', 1), True)

if __name__ == '__main__':
    unittest.main()
class FileSystem:
    def __init__(self):
        self.map = {'': 0}
        self.callbackMap = {}

    def create(self, path, value):
        if path in self.map:
            return False
        idx = path.rfind('/')
        if path[:idx] not in self.map:
            return False
        self.map[path] = value
        return True

    def set(self, path, value):
        if path not in self.map:
            return False
        self.map[path] = value
        curr = path
        while curr:
            if curr in self.callbackMap:
                self.callbackMap[curr]()
            curr = curr[:curr.rfind('/')]
        return True
        # for s in self.callbackMap:
        #     if s.startswith(path):
        #         self.callbackMap[s]()
        # return True

    def get(self, path):
        if path not in self.map:
            return -1
        return self.map[path]

    def watch(self, path):
        if path not in self.map:
            return

        def callback():
            print(path)

        self.callbackMap[path] = callback


# fileSystem = FileSystem()
# print(fileSystem.create('/a', 1))
# print(fileSystem.get('/a'))
# print(fileSystem.create('/a/b', 2))
# print(fileSystem.get('/a/b'))
# print(fileSystem.create('/c/d', 3))
# fileSystem.set('/a/b', 4)
# print(fileSystem.get('/a/b'))
# fileSystem.watch('/a')
# fileSystem.watch('/a/b')
# fileSystem.set('/a/b', 5)
# fileSystem.set('/a', 5)
# print(fileSystem.get('/a/b'))


class Node:
    def __init__(self, key, val, callBack, children):
        self.key = key
        self.val = val
        self.callBack = callBack
        self.children = children


class FileSystem2:  # Trie
    def __init__(self):
        self.root = Node('', 0, None, {})

    def create(self, key, val):
        node = self.root
        strs = key.split('/')
        for i in range(1, len(strs) - 1):
            c = strs[i]
            if c not in node.children:
                return False
            node = node.children[c]
        toAdd = strs[-1]
        if toAdd in node.children:
            return False
        node.children[toAdd] = Node(toAdd, val, None, {})
        return True

    def get(self, key):
        node = self.root
        strs = key.split('/')
        for i in range(1, len(strs)):
            c = strs[i]
            if c not in node.children:
                return -1
            node = node.children[c]
        return node.val

    def set(self, key, val):
        node = self.root
        strs = key.split('/')
        callBacks = []
        for i in range(1, len(strs)):
            c = strs[i]
            if c not in node.children:
                return False
            node = node.children[c]
            if node.callBack:
                callBacks.append(node.callBack)
        while callBacks:
            callBacks.pop()()

        # def dfs_callback(node):
        #     if node.callBack:
        #         node.callBack()
        #     for c in node.children:
        #         dfs_callback(node.children[c])
        # dfs_callback(node)
        node.val = val
        return True

    def watch(self, key, alert):
        node = self.root
        strs = key.split('/')
        for i in range(1, len(strs)):
            c = strs[i]
            if c not in node.children:
                return
            node = node.children[c]

        def callBack():
            print(alert)

        node.callBack = callBack

fileSystem = FileSystem2()
print(fileSystem.create('/a', 1))
print(fileSystem.get('/a'))
print(fileSystem.create('/a/b', 2))
print(fileSystem.get('/a/b'))
print(fileSystem.create('/c/d', 3))
fileSystem.set('/a/b', 4)
print(fileSystem.get('/a/b'))
fileSystem.watch('/a', '/a call back')
fileSystem.watch('/a/b', '/a/b call back')
fileSystem.set('/a', 5)
print(fileSystem.get('/a/b'))

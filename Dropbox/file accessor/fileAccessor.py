import collections

# recursive / iterative
class fileAccess:
    def __init__(self):
        self.parent = {}
        self.access = set()
        self.nonInherient = set()

    def setNonInherient(self, nonInherient):
        self.nonInherient = nonInherient

    def buildAccess(self, access):
        self.access = access

    def buildMap(self, folders):
        for i, j in folders:
            self.parent[i] = j

    def hasAccess(self, folder):
        # O(logn) is balanced, O(n) in worst case
        # recursion, maximum recursion depth might be exceeded
        # if folder in self.access:
        #     return True
        # if not folder or folder not in self.parent:
        #     return False
        # res = self.hasAccess(self.parent[folder])
        # if res:
        #     self.access.add(folder)
        # return res
        tep = folder
        while folder and folder in self.parent and folder not in self.access and folder not in self.nonInherient:
            folder = self.parent[folder]
        if folder in self.access:
            self.access.add(tep)
            return True
        return False

    def simplify(self):
        simplified = set()
        for fold in self.access:
            tep = fold
            while fold and self.parent[fold] not in self.access:
                fold = self.parent[fold]
            if not fold:
                simplified.add(tep)
        return simplified


# bfs
class fileAccess2:
    def __init__(self):
        self.children = collections.defaultdict(set)
        self.access = set()
        self.not_access = set()

    def buildAccess(self, access):
        self.access = access

    def buildMap(self, folders):
        for i, j in folders:
            if j:
                self.children[j].add(i)

    def hasAccess(self, folder):
        if folder in self.access:
            return True
        if folder in self.not_access:
            return False
        dq = collections.deque(self.access)
        seen = set(self.access)
        while dq:
            cur = dq.popleft()
            for child in self.children[cur]:
                if child not in seen:
                    seen.add(child)
                    if child == folder:
                        self.access.add(folder)
                        return True
                    dq.append(child)
        self.not_access.add(folder)
        return False

fa = fileAccess()
fa.buildMap([
    ('A', None),
    ('B', 'A'),
    ('C', 'B'),
    ('D', 'B'),
    ('E', 'A'),
    ('F', 'E'),
    ('G', 'F')
])

fa.setNonInherient({'F'})

fa.buildAccess({'A'})
print(fa.hasAccess('F'))
print(fa.hasAccess('D'))
print(fa.simplify())

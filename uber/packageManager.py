import collections
class PackageManager:
    def __init__(self):
        self.dependencies = collections.defaultdict(set)

    def addPackage(self, packageName, dependencies):
        self.dependencies[packageName] |= set(dependencies)
        self.dependencies[packageName].discard(packageName)

    def getDependency(self, packageName):
        res = set()
        def getAllPackages(curr):
            if curr == packageName or curr in res: return
            res.add(curr)
            for d in self.dependencies[curr]:
                getAllPackages(d)
        for d in self.dependencies[packageName]:
            getAllPackages(d)
        self.dependencies[packageName] |= res
        return self.dependencies[packageName]

packageManager = PackageManager()
packageManager.addPackage('1', ['1','2','3','4'])
packageManager.addPackage('2', ['1','5'])
print(packageManager.dependencies['1'])
print(packageManager.dependencies['2'])
print(packageManager.getDependency('1'))
print(packageManager.getDependency('2'))

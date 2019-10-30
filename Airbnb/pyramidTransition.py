import collections


class Solution:
    def pyramidTransition(self, bottom, allowed):
        c = collections.defaultdict(set)
        for a in allowed:
            c[a[:-1]].add(a[-1])

        def dfs(bottom, idx, nxt):
            if len(bottom) == 1: return True
            if idx == len(bottom) - 1: return dfs(nxt, 0, "")
            for a in c[bottom[idx:idx + 2]]:
                if dfs(bottom, idx + 1, nxt + a): return True
            return False

        return dfs(bottom, 0, "")

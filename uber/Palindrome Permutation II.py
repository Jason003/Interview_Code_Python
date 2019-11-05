import collections


class Solution:
    def generatePalindromes(self, s):
        if not s: return []
        cnt = collections.Counter(s)
        appearOdd = [k for k, v in cnt.items() if v % 2]
        if len(appearOdd) > 1: return []
        res = set()
        for k in cnt:
            cnt[k] //= 2

        def dfs(cur):
            if len(cur) == len(s) // 2:
                res.add(cur)
                return
            for k in cnt:
                if cnt[k] > 0:
                    cnt[k] -= 1
                    dfs(cur + k)
                    cnt[k] += 1

        dfs('')
        if len(appearOdd) == 0:
            return [s + s[::-1] for s in res]
        else:
            return [s + appearOdd[0] + s[::-1] for s in res]

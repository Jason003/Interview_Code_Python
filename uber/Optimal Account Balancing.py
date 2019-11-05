import collections


class Solution:
    def minTransfers(self, transactions) -> int:
        balance = collections.Counter()
        for i, j, v in transactions:
            balance[i] -= v
            balance[j] += v
        value = [v for v in balance.values() if v != 0]
        n = len(value)

        def dfs(idx):
            while idx < n and value[idx] == 0:
                idx += 1
            if idx == n:
                return 0

            res = float('inf')
            for i in range(idx + 1, n):
                if value[i] * value[idx] < 0:
                    value[i] += value[idx]
                    res = min(res, dfs(idx + 1) + 1)
                    value[i] -= value[idx]
            return res

        return dfs(0)

class bankSystem:
    def __init__(self, accounts, thresholds):
        self.accounts = accounts
        self.thresholds = thresholds

    def transfer(self):
        netAccounts = [[self.accounts[i] - self.thresholds[i], i] for i in self.accounts if i in self.thresholds]

        netAccounts.sort(reverse=True)

        if sum([i for i, j in netAccounts] or [0]) < 0:
            print('impossible!')
            return

        n = len(netAccounts)

        def dfs(idx):
            while idx < n and netAccounts[idx][0] == 0:
                idx += 1
            if idx == n:
                return
            for i in range(idx + 1, n):
                if netAccounts[i][0] < 0:
                    print(netAccounts[idx][1] + '->' + netAccounts[i][1] + ':' + str(netAccounts[idx][0]))
                    netAccounts[i][0] += netAccounts[idx][0]
                    netAccounts[idx][0] = 0
                    dfs(idx + 1)

        dfs(0)

bankSystem({'A': 1500, 'B': 0, 'C':0}, {'A': 0, 'B': 700, 'C':800}).transfer()

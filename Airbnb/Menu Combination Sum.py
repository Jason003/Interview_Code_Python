def MenuCombinationSum1(prices, target): # one dish can be used for more than once
    eps = 10 ** (-5)
    res = []
    prices.sort()
    def dfs(idx, curr, summ):
        if summ - target > eps:
            return
        if abs(summ - target) < eps:
            res.append(tuple(curr))
            return
        for i in range(idx, len(prices)):
            if i > idx and prices[i] == prices[i - 1]: continue
            dfs(i, curr + [prices[i]], summ + prices[i]) # one dish can be used more than one time
    dfs(0, [], 0)
    return res

def MenuCombinationSum2(prices, target):  # one dish can't be used for more than once
    eps = 10 ** (-5)
    res = []
    prices.sort()

    def dfs(idx, curr, summ):
        if summ - target > eps:
            return
        if abs(summ - target) < eps:
            res.append(tuple(curr))
            return
        for i in range(idx, len(prices)):
            if i > idx and prices[i] == prices[i - 1]: continue
            dfs(i + 1, curr + [prices[i]], summ + prices[i])  # one dish can be used more than one time

    dfs(0, [], 0)
    return res

print(MenuCombinationSum2([2.40, 0.01, 6.00, 0.01, 2.58], 2.42))

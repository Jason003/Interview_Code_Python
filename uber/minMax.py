
def PredictTheWinner(nums):
    mem = {} # represents the net score first player can get
    def dfs(i, j):
        if (i, j) in mem:
            return mem[i, j]
        if i > j: return 0
        res = max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))
        mem[i, j] = res
        return res
    netGain = dfs(0, len(nums) - 1)
    return (sum(nums) + netGain) // 2
print(PredictTheWinner([1,2,3,4,5,6]))
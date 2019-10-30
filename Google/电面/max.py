def get_max_sum(l, k):
    currSum = sum(l[:k])
    max_sum = currSum
    i = 1
    while i <= k:
        currSum = currSum - l[k - i] + l[-i]
        max_sum = max(max_sum, currSum)
        i += 1
    return max_sum

print(get_max_sum([1,100,2,2], 2))
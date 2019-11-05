import math
class Solution:
    def searchRange(self, nums, target):
        l, r = 0, len(nums) - 1
        res = [-1, -1]
        while l < r:
            m = (r - l) // 2 + l
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if not nums or nums[l] != target: return [-1, -1]
        res[0] = l
        l, r = 0, len(nums) - 1
        while l < r:
            m = math.ceil((r + l) / 2)
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        res[1] = r
        return res
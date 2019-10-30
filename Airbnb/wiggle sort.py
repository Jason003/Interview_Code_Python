import random
class Solution(object):
    def wiggleSort(self, nums):
        if len(nums) == 1:
            return
        n = len(nums)

        # Index-rewiring.
        f = lambda i: (1 + 2 * (i)) % (n | 1)

        mid = self.findKthSmallest(nums, len(nums) // 2)

        # 3 way partition
        i, j, k = 0, 0, n - 1

        while j <= k:
            if (nums[f(j)] > mid):
                nums[f(i)], nums[f(j)] = nums[f(j)], nums[f(i)]
                i += 1
                j += 1
            elif nums[f(j)] < mid:
                nums[f(j)], nums[f(k)] = nums[f(k)], nums[f(j)]
                k -= 1
            else:
                j += 1

    def findKthSmallest(self, nums, k):
        # quick select
        def quickSelect(nums, l, r, k):
            randIdx = random.randint(l, r)
            nums[randIdx], nums[r] = nums[r], nums[randIdx]
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(nums, p + 1, r, k)
            else:
                return quickSelect(nums, l, p - 1, k)

        return quickSelect(nums, 0, len(nums) - 1, k)
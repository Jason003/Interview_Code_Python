class Solution(object):
    def wiggleSort(self, nums):
        if len(nums) == 1:
            return
        n = len(nums)

        # Index-rewiring.
        # f = lambda i:(1+2*(i)) % (n|1)

        median = self.findKthSmallest(nums, len(nums) // 2)

        # 3 way partition
        # i, j, k = 0, 0, n-1

        # while j <= k:
        #     if (nums[f(j)] > mid):
        #         nums[f(i)], nums[f(j)] = nums[f(j)], nums[f(i)]
        #         i += 1
        #         j += 1
        #     elif nums[f(j)] < mid:
        #         nums[f(j)], nums[f(k)] = nums[f(k)], nums[f(j)]
        #         k -= 1
        #     else:
        #         j += 1

        odd = 1
        even = n - 2 if n % 2 == 0 else n - 1
        tmp = [0 for _ in range(n)]
        for i in range(n):
            if nums[i] > median:
                tmp[odd] = nums[i]
                odd += 2
            elif nums[i] < median:
                tmp[even] = nums[i]
                even -= 2
        while odd < n:
            tmp[odd] = median
            odd += 2
        while even >= 0:
            tmp[even] = median
            even -= 2
        for i in range(n):
            nums[i] = tmp[i]

    def findKthSmallest(self, nums, k):
        # quick select
        def quickSelect(nums, l, r, k):
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

'''
Notice that by placing the median in it's place in the array we divided the array in 3 chunks: all numbers less than median are in one side, all numbers larger than median are on the other side, median is in the dead center of the array.

We want to place any a group of numbers (larger than median) in odd slots, and another group of numbers (smaller than median) in even slots. So all numbers on left of the median < n / 2 should be in odd slots, all numbers on right of the median > n / 2 should go into even slots (remember that median is its correct place at n / 2)

PS: I'm ignoring the discussion of odd/even array length for simplicity.

So let's think about the first group in the odd slots, all numbers is the left side of the array should go into these odd slots. What's the formula for it? Naturally it would be:
(1 + 2 x index) % n

All these indexes are less than n / 2 so multiplying by 2 and add 1 (to make them go to odd place) and then mod by n will always guarantee that they are less than n.

Original Index => Mapped Index
0 => (1 + 2 x 0) % 6 = 1 % 6 = 1
1 => (1 + 2 x 1) % 6 = 3 % 6 = 3
2 => (1 + 2 x 2) % 6 = 5 % 6 = 5

These are what's less than median, if we continue this with indexes 3, 4, 5 we will cycle again:
3 => (1 + 2 x 3) % 6 = 7 % 6 = 1
4 => (1 + 2 x 4) % 6 = 9 % 6 = 3
5 => (1 + 2 x 5) % 6 = 11 % 6 = 5

and we don't want that, so for indexes larger than n/2 we want them to be even, (n|1) does that exactly. What n|1 does it that it gets the next odd number to n if it was even
if n = 6 for example 110 | 1 = 111 = 7
if n = 7 for example 111 | 1 = 111 = 7

and this is what we want, instead of cycling the odd numbers again we want them to be even, and odd % odd number is even so updating the formula to :
(1 + 2*index) % (n | 1)

Then we have:
3 => (1 + 2 x 3) % 7 = 7 % 7 = 0
4 => (1 + 2 x 4) % 7 = 9 % 7 = 2
5 => (1 + 2 x 5) % 7 = 11 % 7 = 4
'''
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

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        k = (m + n - 1) // 2
        lo, hi = 0, m - 1
        while lo <= hi:
            m1 = (hi - lo) // 2 + lo
            m2 = k - m1
            if nums1[m1] > nums2[m2]:
                hi = m1 - 1
            elif nums1[m1] < nums2[m2]:
                lo = m1 + 1
            else:
                return nums1[m1]
        a = max(nums1[lo - 1] if lo > 0 else -float('inf'), nums2[k - lo] if k - lo >= 0 else -float('inf'))
        if (m + n) & 1: return a
        b = min(nums1[lo] if lo < m else float('inf'), nums2[k - lo + 1] if k - lo + 1 < n else float('inf'))
        return (a + b) / 2

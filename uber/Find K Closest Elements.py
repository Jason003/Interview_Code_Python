class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        # O(nlogn)
        # return sorted(sorted(arr, key = lambda i: (abs(i - x), i))[:k])

        # O(log(n - k) + k)
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if x - arr[mi] > arr[mi + k] - x:
                lo = mi + 1
            else:
                hi = mi
        return arr[lo: lo + k]
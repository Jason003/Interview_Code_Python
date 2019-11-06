class Solution:
    def maxChunksToSorted(self, arr) -> int:
        res = 0
        curMax = -1
        for i, a in enumerate(arr):
            curMax = max(curMax, a)
            if curMax == i:
                res += 1
        return res


'''class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length, res = 0;
        int[] maxOfLeft = new int[n], minOfRight = new int[n];
        maxOfLeft[0] = arr[0];
        minOfRight[n - 1] = arr[n - 1];
        for(int i = 1; i < n; ++i)
            maxOfLeft[i] = Math.max(arr[i], maxOfLeft[i - 1]);
        for(int i = n - 2; i >= 0; --i)
            minOfRight[i] = Math.min(arr[i], minOfRight[i + 1]);
        for(int i = 0; i < n - 1; ++i) {
            if(maxOfLeft[i] <= minOfRight[i + 1]) ++res;
        }
        return res + 1;
    }
}'''

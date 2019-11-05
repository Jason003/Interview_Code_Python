class Solution:
    def canCross(self, s):
        stones = set(s)
        step = 1
        for i in range(len(s) - 1):
            if s[i + 1] - s[i] > step: return False
            step += 1

        def helper(start, end, step):
            if start == end: return True
            if start not in stones: return False
            return helper(start + step + 1, end, step + 1) or helper(start + step, end, step) or step > 1 and helper(
                start + step - 1, end, step - 1)

        return helper(1, s[-1], 1)

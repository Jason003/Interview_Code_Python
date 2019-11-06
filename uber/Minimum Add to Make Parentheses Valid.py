
class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l, r, res = 0, 0, 0
        for c in S:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0: l -= 1
                else: r += 1
            res = max(res, r)
        return res + l
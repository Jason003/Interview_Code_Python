class Solution:
    def fractionToDecimal(self, a: int, b: int) -> str:
        d = {}
        if a % b == 0: return str(a // b)
        neg = False
        if a * b < 0:
            neg = True
            a, b = abs(a), abs(b)
        before = str(a // b)
        rem = a - (a // b) * b
        after = ''
        while rem:
            if rem in d:
                return ('-' if neg else '') + before + '.' + after[:d[rem]] + '(' + after[d[rem]:] + ')'
            d[rem] = len(after)
            digit = rem * 10 // b
            after += str(digit)
            rem = rem * 10 - digit * b
        return ('-' if neg else '') + before + '.' + after

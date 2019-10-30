class GuessNumber:

    def __init__(self, target):
        self.target = target
        self.pre = ['1111', '2222', '3333', '4444', '5555', '6666']

    def guessServer(self, candidate): # return the number of correct number
        return sum(i == j for i, j in zip(self.target, candidate))

    def guess(self):
        digits = [] # digits for final answer
        for pre in self.pre:
            digits += [pre[0]] * self.guessServer(pre)
        res = ['#'] * 4
        matches = 0
        for d in digits:
            for i in range(4):
                if res[i] == '#':
                    res[i] = d
                    if self.guessServer(''.join(res)) == matches + 1:
                        matches += 1
                        break
                    res[i] = '#'
        return ''.join(res)

for i in range(1000, 6000):
    s = str(i)
    if all(1 <= int(c) <= 6 for c in s):
        assert s == GuessNumber(s).guess()



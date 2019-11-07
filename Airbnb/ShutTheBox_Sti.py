import random


class ShutTheBox:
    def __init__(self, n=10):
        """
        :param n: excluded
        """
        self.max_num = n
        self.nums = [i for i in range(1, n)]  # using 1 to denote every number 9,8, 7... 1

    def rollDice(self):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        return (r1, r2)

    def getValidComb(self, diceSum):  # get all valid combinations
        n = self.max_num
        numList = []  # numbers can be choosed
        for i in range(1, n):
            if self.nums[i - 1] != 0:
                numList.append(i)

        cmbs = []

        def dfs(idx, curr, summ):
            if summ > diceSum: return
            if summ == diceSum:
                cmbs.append(curr)
                return
            for i in range(idx, len(numList)):
                dfs(i + 1, curr + [numList[i]], summ + numList[i])

        dfs(0, [], 0)
        return cmbs

    def getNextAction(self, diceSum):
        cmb = self.getValidComb(diceSum)
        if not cmb:
            print("can not move forward")
            print("game end! \n")
            return False
        print("combination to choose: ")
        for i, l in enumerate(cmb):
            print(i, l)

        print("enter the index: ")
        idx = int(input())
        while idx < 0 or idx >= len(cmb):
            print("out of bound, please choose again")
            idx = int(input())

        print("you choose: ", end="")
        print(cmb[idx])
        print("")
        choiceCmb = cmb[idx]
        self.getNextState(choiceCmb)  # update the state
        return choiceCmb

    def getNextState(self, comb):
        for b in comb:
            self.nums[b - 1] = 0


def playGame(maxTurns):
    cnt = 0
    while cnt <= maxTurns:
        stb = ShutTheBox(10)
        while True:
            print("curState:  ", end="")
            print(stb.nums)
            r1, r2 = stb.rollDice()
            diceSum = r1 + r2
            print("Rolled %d and %d, the sum is %d" % (r1, r2, diceSum))
            cmb = stb.getNextAction(diceSum)
            if not cmb: break
        cnt += 1


playGame(2)

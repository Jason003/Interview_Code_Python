import random
class ShutTheBox:
    def __init__(self):
        self.nOfState = (1 << 10)
        self.nextStates =[[-1 for i in range(13)] for j in range(self.nOfState)]
        self.chanceToWin = [[0 for i in range(13)] for j in range(self.nOfState)]
        self.sumChance =[0 for _ in range(13)]

        # calculate the probability of every sum
        for i in range(1, 7):
            for j in range(1, 7):
                self.sumChance[i + j ] += 1 / 36

        # get choices
        for diceSum in range(2, 13):
            self.getBestChoice(self.nOfState - 1, diceSum)

    def pickCombination(self, state, diceSum):
        if self.nextStates[state][diceSum] == -2: return None
        return self.getDiff(state, self.nextStates[state][diceSum])
        # get the number we can use from current state to next state


    def getDiff(self, state, nextState):
        ans = []
        if nextState == -2: return None
        self.printState(state)
        self.printState(nextState)
        for i in range(1, 10):
            mask = 1 << i
            if (mask & state) > 0 and (mask & nextState) == 0:
                ans.append(i)
        return ans

    def getBestChoice(self, state, diceSum):
        if self.nextStates[state][diceSum] != -1:
            return self.chanceToWin[state][diceSum]
        # best cases
        if state == 0 or state == 1:
            self.chanceToWin[state][diceSum] = 1
            self.nextStates[state][diceSum] = 0
            return 1
        # get combination functions
        choices = self.getChoicesOfCombination(state, diceSum)
        bestExp = 0
        bestNxtState = -2
        for cmb in choices:
            nxt = self.getNextState(state, cmb)
            exp = 0
            for c in range(2, 13):
                exp += self.sumChance[c] * self.getBestChoice(nxt, c)
            if exp > bestExp:
                bestExp = exp
                bestNxtState = nxt

        self.chanceToWin[state][diceSum] = bestExp
        self.nextStates[state][diceSum] = bestNxtState
        return bestExp

    def getChoicesOfCombination(self, state, diceSum):
        nums = []
        for i in range(1, 10):
            if (state &(1<<i) !=0):
                nums.append(i)
        ans = []
        self.dfs(nums, ans, 0, diceSum,0, [])
        return ans

    def dfs(self, nums, ans, index, target, curSum, path):
        if curSum > target: return
        if curSum == target:
            ans.append(path[:])
            return
        for j in range(index, len(nums)):
            self.dfs(nums, ans, j + 1, target, curSum + nums[j], path + [nums[j]])


    def getNextState(self, state, comb):
        for b in comb:
            state -= (1<<b)
        return state

    def printState(self, state):
        ans = []
        for i in range(1, 10):
            if state & (1<<i) >0:
                ans.append(i)
        print(ans)


class PlayGame:
    def rollDice(self):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        return  r1 + r2

    def runOnce(self, stb):
        curState = (1 << 10) - 1 # all numbers can be chosen
        while True:
            # stb.printState(curState)
            c = self.rollDice()
            cmb = stb.pickCombination(curState, c)
            if not cmb : return False
            else:
                curState = stb.getNextState(curState, cmb)
                if curState <= 1:
                    return True

    def playGame(self):
        stb = ShutTheBox()
        maxTrial = 1
        cnt = 0
        for i in range(maxTrial):
            if self.runOnce(stb):
                cnt += 1

        print(cnt * 1.0 / maxTrial)

test = PlayGame()
test.playGame()

# test2 = ShutTheBox_stimulate()
# test2.play(100, 10, True)
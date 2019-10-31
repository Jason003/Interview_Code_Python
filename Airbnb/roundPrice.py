import math
def roundPrice(A):
    # attention: in python3, round(1.5) = 1 !!!
    def round(x):
        fac = x - math.floor(x)
        return math.ceil(x) if fac >= 0.5 else math.floor(x)

    if not A:
        return A
    roundSum = sum(map(round, A))
    sumRound = round(sum(A))
    print(roundSum)
    print(sumRound)
    res = [round(a) for a in A]
    if roundSum == sumRound:
        return res
    elif roundSum > sumRound:
        cnt = roundSum - sumRound # need to make cnt number to round(number) - 1
        nums = sorted([(a - math.floor(a), a, i) for i, a in enumerate(A)])
        for fac, a, i in nums:
            if fac >= 0.5 and cnt > 0:
                res[i] = math.floor(a)
                cnt -= 1
            else:
                res[i] = round(a)
        return res
    else:
        cnt = sumRound - roundSum  # need to make cnt number to round(number) + 1
        nums = sorted([(a - math.floor(a), a, i) for i, a in enumerate(A)])[::-1]
        for fac, a, i in nums:
            if fac < 0.5 and cnt > 0:
                res[i] = math.ceil(a)
                cnt -= 1
            else:
                res[i] = round(a)
        return res

print(roundPrice([1,2,3,4]))
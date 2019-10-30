def addSubstract(A):
    res = 0
    sign = 1
    for a in A:
        res += sign * a
        sign = -sign
    return res
print(addSubstract([5,2,3,1,4]))
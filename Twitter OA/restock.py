def solution(A, target):
    summ = 0
    for i in A:
        summ += i
        if summ >= target:
            return summ - target
    return target - summ


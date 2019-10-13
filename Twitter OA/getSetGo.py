def solution(input, requiredCals):
    summ = {0}
    for i in input:
        summ |= {i + j for j in summ}
        if requiredCals in summ:
            return True
    return False

print(solution([2,3,15,1,16], 8))
def solution(n):
    l = list(map(int, list(str(n))))
    mul = 1
    for i in l:
        mul *= i
    return mul - sum(l)
print(solution(230))
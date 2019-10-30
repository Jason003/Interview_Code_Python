def solution(A):
    def judge(a):
        return any([int(i) % 2 == 0 for i in str(a)])
    return sum([judge(a) for a in A] or [0])
print(solution([12, 3, 5, 3456]))
def solution(A):
    if not A: return
    m, n = len(A), len(A[0])
    x, y = 0, n
    while x < m:
        while y - 1 >= 0 and A[x][y - 1] == 1:
            y -= 1
        x += 1
    return y


print(solution([[0, 0, 0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0]]))

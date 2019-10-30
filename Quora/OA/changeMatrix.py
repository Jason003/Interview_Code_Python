def solution(A, Q):
    n = len(A)
    def change(idx):
        if idx == 1 or idx == 0:
            for i in range(n):
                for j in range(i + 1):
                    A[i][j], A[j][i] = A[j][i], A[i][j]
            if idx == 1:
                return
            for i in range(n):
                l, r = 0, n - 1
                while l < r:
                    A[i][l], A[i][r] = A[i][r], A[i][l]
                    l += 1
                    r -= 1
            return
        elif idx == 2:
            for i in range(n):
                for j in range(n - i):
                    A[i][j], A[-j-1][-i-1] = A[-j-1][-i-1], A[i][j]
    for q in Q:
        change(q)
    return A
print(solution([[1,2,3],[4,5,6],[7,8,9]], [0,1,2]))
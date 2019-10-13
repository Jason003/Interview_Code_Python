def solution(A):

    def smallerOrEqualTo(A):
        stack = []
        smallerIndex = [-1] * len(A)
        for i, a in enumerate(A):
            while stack and a <= A[stack[-1]]:
                smallerIndex[stack.pop()] = i
            stack.append(i)
        return smallerIndex

    smallerIndexArr = smallerOrEqualTo(A)

    res = []
    for i, a in enumerate(A):
        if smallerIndexArr[i] != -1:
            res.append(a - A[smallerIndexArr[i]])
        else:
            res.append(a)
    print(sum(res))
    print(' '.join(map(str, res)))

solution([2,3,1,2,4,2])

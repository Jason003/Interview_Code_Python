def largest_subarray(A, k):
    idx = 0
    for i in range(1, len(A) - k + 1):
        if A[idx] < A[i]:
            idx = i
    return A[idx : idx + k]

print(largest_subarray([1,4,3,2,5], 4))
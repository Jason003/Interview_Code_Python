'''
Explanation
Sort the jobs by endTime.

dp[time] = profit means that within the first time duration,
we cam make at most profit money.
Intial dp[0] = 0, as we make profit = 0 at time = 0.

For each job = [s, e, p], where s,e,p are its start time, end time and profit,
Then the logic is similar to the knapsack problem.
If we don't do this job, nothing will be changed.
If we do this job, binary search in the dp to find the largest profit we can make before start time s.
So we also know the maximum cuurent profit that we can make doing this job.

Compare with last element in the dp,
we make more money,
it worth doing this job,
then we add the pair of [e, cur] to the back of dp.
Otherwise, we'd like not to do this job.


Complexity
Time O(NlogN) for sorting
Time O(NlogN) for binary search for each job
Space O(N)
'''



import bisect
def jobScheduling(startTime, endTime, profit):
    n = len(startTime)
    event = sorted([(startTime[i], endTime[i], profit[i], i) for i in range(n)], key=lambda x: x[1])
    dp = [(0, 0, -1)]
    path = {}
    final_idx = -1
    for s, e, v, i in event:
        idx = bisect.bisect(dp, (s + 1,)) - 1 # find the largest end time that is less than s
        if dp[idx][1] + v > dp[-1][1]:
            dp.append((e, dp[idx][1] + v, i))
            path[i] = dp[idx][-1]
            final_idx = i
    path_arr = []
    while final_idx in path:
        path_arr.append(final_idx)
        final_idx = path[final_idx]
    return dp[-1][1], path_arr[::-1]





def jobScheduling2(startTime, endTime, profit):
    n = len(startTime)
    event = sorted([(startTime[i], endTime[i], profit[i], i) for i in range(n)], key=lambda x: x[1])
    dp = [c for a, b, c, d in event]
    res = 0
    path = {}
    final_index = -1
    for i in range(n):
        for j in range(i):
            if event[j][1] <= event[i][0] and dp[j] + event[i][2] > dp[i]:
                dp[i] = dp[j] + event[i][2]
                path[event[i][-1]] = event[j][-1]
        if res < dp[i]:
            res = dp[i]
            final_index = event[i][-1]
    arr = []
    while final_index in path:
        arr.append(final_index)
        final_index = path[final_index]
    return res, [final_index] + arr[::-1]


startTime = [631,919,696,968,618,133,263,517,265,290,741,646,534,605,978,584,937,37,666,446,264,58,461,648,382,783,719,958,247,837,547,978,169,172,545,326,720,232,121,335,575,496,701,662,201,641,158,976,658,888,645,338,401,627,803,716,139,243,382,592,287,743,683,162,220,871,957,694,108,318,390,416,855,922,293,116,574,759,50,690,314,424,607,894,520,972,85,214,118,992,197,865,826,160,19,583,520,585,268,872]
endTime = [811,960,887,986,685,440,339,709,682,510,897,896,588,906,980,604,984,676,788,748,814,207,852,905,478,880,732,986,327,864,739,990,221,354,594,763,962,273,139,416,852,887,809,959,718,919,175,994,897,987,651,530,939,819,807,874,956,651,809,952,442,861,990,535,732,926,965,900,195,595,492,432,950,963,857,280,712,794,751,732,754,531,710,958,694,982,884,352,729,996,253,947,940,268,442,763,963,862,760,884]
profit = [7,25,35,83,75,89,61,23,28,97,43,100,92,29,97,44,52,55,91,18,27,7,34,41,11,12,20,89,50,96,80,36,90,79,91,18,12,50,95,32,78,66,17,59,60,39,18,75,73,75,60,49,75,86,67,10,76,6,40,81,35,93,29,96,94,92,99,3,76,88,97,64,79,39,5,81,46,82,82,86,43,54,36,35,90,26,65,59,22,44,84,14,97,99,81,35,41,15,82,30]

print(jobScheduling(startTime, endTime, profit))
print(jobScheduling2(startTime, endTime, profit))



def _search(A, k):  # find the largest index i where A[i]
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mi = (lo + hi) // 2
        if A[mi] == k:
            return mi
        elif A[mi] < k:
            lo = mi + 1
        else:
            hi = mi - 1
    return lo
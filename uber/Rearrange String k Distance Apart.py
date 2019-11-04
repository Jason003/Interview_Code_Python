import heapq, collections


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s
        cnt = collections.Counter(s)
        heap = []
        for c, freq in cnt.items():
            heapq.heappush(heap, (-freq, c))
        res = []
        while heap:
            temp = []
            for _ in range(k):
                if not heap:
                    return '' if len(res) != len(s) else ''.join(res)
                negFreq, c = heapq.heappop(heap)
                res.append(c)
                if negFreq != -1:
                    temp.append((negFreq + 1, c))
            heap += temp
            heapq.heapify(heap)
        return ''.join(res)


print(Solution().rearrangeString("aaadbbcc", 2))

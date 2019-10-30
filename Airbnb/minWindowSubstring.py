import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = collections.Counter(t)
        start, end, n = 0, 0, len(s)
        mark = len(t)
        res = ''
        while end < n:
            cnt[s[end]] -= 1
            if cnt[s[end]] >= 0:
                mark -= 1
            while mark == 0:
                if not res or len(res) > end - start + 1:
                    res = s[start: end + 1]
                if cnt[s[start]] == 0:
                    mark += 1
                cnt[s[start]] += 1
                start += 1
            end += 1
        return res

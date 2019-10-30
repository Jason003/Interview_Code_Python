def palindromePairs(words):
    def is_pal(s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    res = set()
    loc = {word: i for i, word in enumerate(words)}
    for i, w in enumerate(words):
        for j in range(len(w) + 1):
            p1, p2 = w[:j], w[j:]
            if is_pal(p1) and p2[::-1] in loc and loc[p2[::-1]] != i:
                res.add((loc[p2[::-1]], i))
            if is_pal(p2) and p1[::-1] in loc and loc[p1[::-1]] != i:
                res.add((i, loc[p1[::-1]]))
    return list(res)

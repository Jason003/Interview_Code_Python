def distinctSubstring(s):
    res = set()
    n = len(s)

    def charToInt(c):
        return ord(c) - ord('a') + 1

    for l in range(1, n + 1): # length of substring
        hashCode = 0
        for i in range(l):
            hashCode = hashCode * 26 + charToInt(s[i])
        res.add(hashCode)
        for i in range(l, n):
            hashCode = (hashCode - charToInt(s[i - l]) * 26 ** (l - 1)) * 26 +  charToInt(s[i])
            res.add(hashCode)
    for i in res:
        print(i)
    return len(res)

print(distinctSubstring('aaaaa'))


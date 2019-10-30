def divisorSubstrings(n, k):
    s = str(n)
    res = set()
    for i in range(len(s) - k + 1):
        if s[i] != '0':
            tep = int(s[i : i + k])
            if n % tep == 0:
                res.add(tep)
    return len(res)
print(divisorSubstrings(555, 1))
def sumOfString(a, b):
    res = []
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        res.append(str(int(a[i] if i >= 0 else 0) + int(b[j] if j >= 0 else 0)))
        i -= 1
        j -= 1
    return ''.join(map(str, res[::-1]))
print(sumOfString('20', '2032'))
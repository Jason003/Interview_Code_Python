def window(n):
    res = ['*' * (n + 2)]
    for _ in range(n - 2):
        res.append('*' + ' ' * n + '*')
    return res + ['*' * (n + 2)]

print(window(6))
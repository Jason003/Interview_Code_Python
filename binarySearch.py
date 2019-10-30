def root(x, n):
    lower = 0
    upper = x

    while upper - lower >= 0.001:
        guess = (upper + lower) / 2
        if guess ** n == x:
            return guess
        elif guess ** n < x:
            lower = guess
        else:
            upper = guess

    return upper

print(root(5, 2))
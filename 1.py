import math
def pthFactor(n, p):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(list(factors))[p - 1]
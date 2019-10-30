def big_number_factorial(n):
    res = [1] * 5000

    def multiply(x, res_size):
        remain = 0
        for i in range(res_size):
            tep = res[i] * x + remain
            res[i] = tep % 10
            remain = tep // 10
        while remain:
            res[res_size] = remain % 10
            res_size += 1
            remain //= 10
        return res_size

    res_size = 1
    for i in range(2, n + 1):
        res_size = multiply(i, res_size)

    return ''.join(map(str, res[:res_size]))[::-1]


import math
for _ in range(1, 100):
    assert str(math.factorial(_)) == big_number_factorial(_)


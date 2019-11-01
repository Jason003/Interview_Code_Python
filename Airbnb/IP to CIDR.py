import math
def ipToCIDR(ip, n):
    # helper function, convert x and steps to CIDR format
    def convert(x, steps):
        return str(x >> 24) + '.' + str((x >> 16) & 255) + '.' + str((x >> 8) & 255) + '.' + str(
            x & 255) + '/' + str(32 - int(math.log2(steps)))

    # find the number represents by ip
    x = 0
    for num in ip.split('.'):
        x = x * 256 + int(num)
    res = []
    # find the number of same prefix with x (we need to find the last position of 1 in binary representation of x)
    while n:
        steps = x & -x  # steps that x can cover e.g. 11111111 00000000 00000000 00001000 -> 8 (from 000 to 111)
        if not steps:
            steps = 1024
        while steps > n: # if steps is greater than n, divide it by 2, e.g. 1000 -> 8, 100 -> 4, 10 -> 2, 1 -> 1
            steps >>= 1
        res.append(convert(x, steps))
        x += steps # add steps to x
        n -= steps # subtract steps we can cover from n
    return res
print(ipToCIDR('0.0.0.0', 10))
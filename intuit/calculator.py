def cal1(s):
    res = 0
    sign = 1
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            res += sign * num
            num = 0
            if c == '+':
                sign = 1
            elif c == '-':
                sign = -1

    print(res + num * sign)

def cal2(s):
    ops = []
    nums = []
    sign = 1
    num = 0
    res = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            res += num * sign
            num = 0
            if c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                ops.append(sign)
                nums.append(res)
                sign = 1
                res = 0
            elif c == ')':
                res = nums.pop() + ops.pop() * res
    return res + sign * num

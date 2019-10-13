def r0(num):
    return str(num).count('7') * 5

def r1(num):
    num = str(num)
    res = 0
    for i in range(len(num) - 1):
        if num[i] == '2' and num[i + 1] == '2':
            res += 6
    return res

def r2(num):
    res = 0
    curr = 1
    num = str(num)
    for i in range(1, len(num)):
        if int(num[i]) - int(num[i - 1]) == -1:
            curr += 1
        else:
            res += curr ** 2
            curr = 1
    return res + curr ** 2

def r3(num):
    return 4 if num % 3 == 0 else 0

def r4(num):
    return sum([int(i) % 2 == 0 for i in str(num)] or [0]) * 3

num = 92228763
print(r0(num))
print(r1(num))
print(r2(num))
print(r3(num))
print(r4(num))
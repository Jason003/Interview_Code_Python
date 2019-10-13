# cache
from functools import wraps

def cahce(function):
    mem = {}
    @wraps(function)
    def wrapper(*args):
        if args in mem:
            return mem[args]
        mem[args] = function(*args)
        return mem[args]
    return wrapper


def getLive(A): # A is the input matrix, it will return a str representing next status of middle row

    def count(i, j):
        cnt = 0
        for ii in (i - 1, i, i + 1):
            for jj in (j - 1, j, j + 1):
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) != (i, j):
                    cnt += int(A[ii][jj])
        return cnt

    if not A: return set()
    m, n = len(A), len(A[0])
    res = []
    for j in range(n):
        if count(1, j) in (2, 3):
            res.append(1)
        else:
            res.append(0)

    return ' '.join(map(str, res)) + '\n'

row = 0

@cahce
def readline(row):
    return i.readline().split()

with open('input.txt', 'r') as i:
    pre = None
    cur = readline(row)
    row += 1
    nxt = readline(row)
    row += 1
    n = len(cur)
    while cur:
        with open('output.txt', 'ab') as o:
            o.write(bytearray(getLive([[0] * n if not pre else pre, cur, [0] * n if not nxt else nxt]), encoding='utf-8'))
        pre, cur, nxt = readline(row - 2), readline(row - 1), readline(row)
        row += 1
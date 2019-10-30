def prefixString(a, b):
    possible = set()
    cur = []
    for s in a:
        cur.append(s)
        possible.add(''.join(cur))
    return all([s in possible for s in b])
print(prefixString(['one', 'two', 'three'], ['onetwo', 'one']))

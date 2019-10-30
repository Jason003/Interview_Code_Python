def compareDict(a, b):
    if type(a) != type(b):
        return False
    if type(a) is str: return a == b
    if set(a.keys()) != set(b.keys()):
        return False
    for i in a:
        if not compareDict(a[i], b[i]):
            return False
    return True

print(compareDict({'a':{'b':'c', 'c':'d'}}, {'a':{'b': 'c'}}))

import collections
def solution(a, b):
    ca = collections.Counter(a)
    cb = collections.Counter(b)
    return set(ca.keys()) == set(cb.keys()) and sorted(list(ca.values())) == sorted(list(cb.values()))
print(solution('aaabbbcccc', 'aaabbbbcccc'))
def compareStrings(A, B):
    strsA = A.split(',')
    strsB = B.split(',')
    m, n = len(strsA), len(strsB)
    frequences = [0] * 11
    result = []

    def count(s):
        return s.count(min(s))

    for a in strsA:
        frequences[count(a)] += 1

    for i in range(len(frequences) - 1):
        frequences[i + 1] += frequences[i]

    for b in strsB:
        freq = count(b)
        result.append(frequences[freq - 1] if freq > 0 else 0)
    return result

print(compareStrings('abcd,aabc,bd', 'aaa,aa'))
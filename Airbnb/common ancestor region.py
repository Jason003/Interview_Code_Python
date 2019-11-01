def solution(A, p, q):
    ansector = {}
    for a in A:
        for child in a[1:]:
            ansector[child] = a[0]

    def getAnsectors(node, seen):
        if node in seen:
            return
        seen.add(node)
        if node in ansector:
            getAnsectors(ansector[node], seen)

    ans1, ans2 = set(), set()
    getAnsectors(p, ans1)
    getAnsectors(q, ans2)
    res = ans1 & ans2
    for candidate in res:
        parents = set()
        getAnsectors(candidate, parents)
        if len(res - parents) == 0:
            return candidate
    return None

print(solution([["Earth", "North America", "South America"],
                ["North America", "United States", "Canada"],
                ["United States", "New York", "Boston"],
                ["Canada", "Ontario", "Quebec"],
                ["South America", "Brazil"]], "Quebec", "New York"))

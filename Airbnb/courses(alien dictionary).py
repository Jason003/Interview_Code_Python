import collections
def courseSchedule1(courseRelation):
    allCourses = set()
    pre = collections.defaultdict(set)
    is_pre = collections.defaultdict(set)
    for i, j in courseRelation:
        allCourses.add(i)
        allCourses.add(j)
        is_pre[j].add(i)
        pre[i].add(j)
    res = []
    seen = set()
    dq = collections.deque([i for i in allCourses if not pre[i]])
    while dq:
        cur = dq.popleft()
        if cur in seen: continue
        seen.add(cur)
        res.append(cur)
        for nei in is_pre[cur]:
            pre[nei].remove(cur)
            if not pre[nei]:
                dq.append(nei)
    return res if len(seen) == len(allCourses) else []

print(courseSchedule1([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('Z', 'Y'), ('Z', 'X'), ('Z', 'G')]))
print(courseSchedule1([('A', 'B'), ('B', 'A')]))

def courseHelper(coursesRelation):
    # time: O(V! + E) space: O(V + E)
    allCourses = set()
    pre = collections.defaultdict(set)
    is_pre = collections.defaultdict(set)
    for i, j in coursesRelation:
        allCourses.add(i)
        allCourses.add(j)
        is_pre[j].add(i)
        pre[i].add(j)

    res = set()

    def dfs(path, seen, course):
        if len(path) == len(allCourses):
            res.add(tuple(path))
            return
        if course in seen or pre[course]:
            return
        mark = set()
        for i in is_pre[course]:
            pre[i].discard(course)
            mark.add(i)
        for i in allCourses - seen:
            dfs(path + [course], seen | {course}, i)
        for i in mark:
            pre[i].add(course)

    for i in allCourses:
        dfs([], set(), i)

    return res

print(courseHelper([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('Z', 'Y'), ('Z', 'X'), ('Z', 'G')]))
print(courseHelper([('A', 'B'), ('B', 'A')]))



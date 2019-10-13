import collections
# person: [[id, name, company]], friendship: [[id, id]]
def getFriendList(person, friendship): # time: O(E + V) space: O(E + V)
    id_name = {}
    for id, name, company in person:
        id_name[id] = name
    friendList = collections.defaultdict(set)
    for a, b in friendship:
        friendList[id_name[a]].add(id_name[b])
        friendList[id_name[b]].add(id_name[a])
    for k, v in friendList.items():
        print(k + ' : ' + ' '.join(list(v)))
    return friendList
# getFriendList([[1,'A','Google'], [2,'B','Google'], [3,'C','Facebook'], [4,'D','Intuit']], [[1,2], [1,3], [1,4]])

def q2(person, friendship):
    id_info = {}
    for id, name, company in person:
        id_info[id] = company
    friendList = collections.defaultdict(set)
    for a, b in friendship:
        if id_info[b] != id_info[a]:
            friendList[a].add(b)
            friendList[b].add(a)
    company_person = collections.defaultdict(set)
    for id, name, company in person:
        company_person[company].add(id)
    for company, workers in company_person.items():
        res1 = len(workers)
        res2 = 0
        for id in workers:
            if friendList[id]:
                res2 += 1
        print(company + ' : ' + str(res1) + ', ' + str(res2))
q2([[1,'A','Google'], [2,'B','Google'], [3,'C','Facebook'], [4,'D','Intuit']], [[1,2], [1,3], [1,4]])
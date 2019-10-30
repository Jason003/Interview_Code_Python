import collections


def display_page(input, size):
    dq = collections.deque()
    host_records = collections.defaultdict(collections.deque)
    for i in input:
        host_records[i.split(',')[0]].append(i)
    for k, v in host_records.items():
        dq.append((v.popleft(), k))
    res = []
    temp = []
    count = 0
    while dq:
        record, host = dq.popleft()
        temp.append(record)
        count += 1
        if host_records[host]:
            dq.append((host_records[host].popleft(), host))
        if count == size:
            res.extend(sorted(temp, key= lambda x : -float(x.split(',')[2])))
            res.append(' ')
            temp = []
            count = 0
    if temp:
        res.extend(sorted(temp, key=lambda x: -float(x.split(',')[2])))
    return res


input = set()
input.add("1,28,310.6,SF")
input.add("4,5,204.1,SF")
input.add("20,7,203.2,Oakland")
input.add("6,8,202.2,SF")
input.add("6,10,199.1,SF")
input.add("1,16,190.4,SF")
input.add("6,29,185.2,SF")
input.add("7,20,180.1,SF")
input.add("6,21,162.1,SF")
input.add("2,18,161.2,SF")
input.add("2,30,149.1,SF")
input.add("3,76,146.2,SF")
input.add("2,14,141.1,San Jose")
input = sorted(list(input), key= lambda x : -float(x.split(',')[2]))
print(display_page(input, 5))

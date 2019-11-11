import collections


def calculate_total_owed(actions):
    def parse(invoice):
        idx = invoice.find(':')
        operation = invoice[:idx].lower()
        strs = invoice[idx + 2:].lower().split('&')
        for str in strs:
            k, v = str.split('=')
            if k == 'id':
                id = v
            elif k == 'amount':
                amount = v
            elif k == 'currency':
                currency = v
        print(operation)
        if operation == 'pay': return (operation, id, 0, 'usd')
        return (operation, id, int(amount), currency)

    d = collections.defaultdict(list)

    for action in actions:
        operation, id, amount, currency = parse(action)
        if currency != 'usd': continue
        if id not in d and operation == 'create':
            d[id].append(('create', int(amount)))
        elif id in d and operation == 'finalize' and len(d[id]) == 1:
            d[id].append(('finalize', int(amount)))
        elif id in d and operation == 'pay' and len(d[id]) == 2:
            d[id].append(('pay', 0))

    res = 0
    for v in d.values():
        print(v)
        if len(v) == 1:
            res += v[0][1]
        elif len(v) == 2:
            res += v[1][1]

    return res
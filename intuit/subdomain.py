import collections
def subdomainVisits(spdomains):
    c = collections.Counter()
    for d in spdomains:
        num, addr = d.split()
        num = int(num)
        words = addr.split('.')
        for i in range(len(words)):
            c['.'.join(words[i:])] += num
    return [str(c[i]) + ' ' + i for i in c]

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

def longestCommonHistory(A, B):
    m, n = len(A), len(B)
    dp = [[[] for i in range(n + 1)] for j in range(m + 1)]
    res = []
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + [A[i - 1]], dp[i][j], key = len)
            else:
                dp[i][j] = []
            res = max(dp[i][j], res, key = len)
    return res

def longestCommonHistory2(A, B):
    m, n = len(A), len(B)
    dp = [[] for i in range(n + 1)]
    res = []
    for i in range(1, len(A) + 1):
        pre = dp[0]
        for j in range(1, len(B) + 1):
            tep = dp[j]
            if A[i - 1] == B[j - 1]:
                dp[j] = pre + [A[i - 1]]
            else:
                dp[j] = []
            res = max(dp[j], res, key = len)
            pre = tep
    return res


'''
String[] purchasedUser = ["203948535", "74545", "b86785"]
String[] history = ["234.64.23.123,2018.10.3,item A","234.457.2345.123,2018.10.3,item A","34.62.34.3,2018.10.3,item B"]
String[] ipaddressUser = ["203948535,234.457.245.123","74545,234.457.2345.123","2347,234.64.23.123"]
'''
def statistics(purchasedUser, history, ipaddressUser):
    counter = {} # key: item, value: (number of buyer, number of visitor)
    purchasedUser = set(purchasedUser)
    ipUser = {} # key: ip, value: user
    for s in ipaddressUser:
        user, ip = s.split(',')
        ipUser[ip] = user

    for h in history:
        ip, time, item = h.split(',')
        counter.setdefault(item, [0, 0])
        counter[item][1] += 1
        if ip in ipUser and ipUser[ip] in purchasedUser:
            counter[item][0] += 1
    return [str(v[0]) + ' of ' + str(v[1]) + ' ' + k for k, v in counter.items()]

print(statistics(["203948535", "56856", "b86785",'313123'], ["234.457.2345.123,2018.10.3,item A","34.62.34.3,2018.10.3,item B"], ["203948535,234.457.2345.123","2347,234.64.23.123",'313123,34.62.34.3']))
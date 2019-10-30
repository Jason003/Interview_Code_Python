import random


def genRandom(n):
    select = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'r', 'f', 'g', 'h', 'd', 'h',
              'p', 'z', 'k', 'm', 'b', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    res = ''
    len = random.randint(6, 10)
    for _ in range(len):
        tep = int(random.randint(0, 20))
        res += select[tep]
    return res


def generateUser():
    for id in range(11):
        userid = 'user' + str(id)
        username = genRandom(6)
        password = genRandom(8)
        email = genRandom(9) + 'gmail.com'
        print("INSERT INTO jl5501.users(user_id, username, email, password) VALUES ('%s', '%s', '%s', '%s');"%(userid, username, email, password))
generateUser()
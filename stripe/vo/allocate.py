import collections
def next_server_number(A):
    # find the first missing number
    A.sort()
    n = len(A)
    for i in range(n):
        if i + 1 != A[i]:
            return i + 1
    return n + 1

class Tracker:
    def __init__(self):
        self.map = collections.defaultdict(set)

    def allocate(self, host_type):
        index = next_server_number(list(self.map[host_type]))
        self.map[host_type].add(index)
        return host_type + str(index)

    def deallocate(self, host_name):
        host_type = ''.join([c for c in host_name if c.isalpha()])
        if host_type not in self.map:
            print('Error! No such host type')
            return
        host_number = int(''.join([c for c in host_name if c.isdigit()]))
        if host_number not in self.map[host_type]:
            print('Error! No such host name')
            return
        self.map[host_type].remove(host_number)


#test
import unittest

class test(unittest.TestCase):
    def test_next_server_number(self):
        self.assertEqual(next_server_number([5,3,1]), 2)

    def test_traker(self):
        traker = Tracker()
        self.assertEqual(traker.allocate('apibox'), 'apibox1')
        self.assertEqual(traker.allocate('apibox'), 'apibox2')
        self.assertEqual(traker.deallocate('apibox1'), None)
        self.assertEqual(traker.allocate('apibox'), 'apibox1')
        self.assertEqual(traker.allocate('sitebox'), 'sitebox1')

if __name__ == '__main__':
    unittest.main()
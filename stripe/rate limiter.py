import time, collections

class RateLimiter:
    def __init__(self, max_number, interval):
        self.timeStamp = collections.defaultdict(collections.deque)
        self.interval = interval
        self.max_number = max_number

    def call(self, id):
        currTime = time.time()
        if len(self.timeStamp[id]) < self.max_number:
            self.timeStamp[id].append(currTime)
            return True
        else:
            if currTime - self.timeStamp[id][0] > self.interval:
                self.timeStamp[id].popleft()
                self.timeStamp[id].append(currTime)
                return True
            else:
                return False

rateLimiter = RateLimiter(5, 2)
for i in range(10):
    print(rateLimiter.call(1))
time.sleep(1)
for i in range(5):
    print(rateLimiter.call(2))




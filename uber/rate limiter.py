import time

class RateLimiter:
    # token bucket
    def __init__(self, max_number, interval):
        self.max_number = max_number
        self.interval = interval
        self.lastTme = time.time()
        self.allowance = max_number # current tokens in the bucket

    def call(self):
        currTime = time.time()
        timeDiff = currTime - self.lastTme
        self.lastTme = currTime
        self.allowance += timeDiff * (self.max_number / self.interval)
        if self.allowance > self.max_number:
            self.allowance = self.max_number
        if self.allowance < 1.0:
            return False
        else:
            self.allowance -= 1.0
            return True

class RateLimiter2: # different clients
    # token bucket
    def __init__(self, max_number, interval):
        self.max_number = max_number
        self.interval = interval
        self.lastTme = {}
        self.allowance = {} # current tokens in the bucket

    def call(self, clientID):
        self.lastTme.setdefault(clientID, time.time())
        self.allowance.setdefault(clientID, self.max_number)
        currTime = time.time()
        timeDiff = currTime - self.lastTme[clientID]
        self.lastTme[clientID] = currTime
        self.allowance[clientID] += timeDiff * (self.max_number / self.interval)

        if self.allowance[clientID] > self.max_number:
            self.allowance[clientID] = self.max_number

        if self.allowance[clientID] < 1.0:
            return False
        else:
            self.allowance[clientID] -= 1.0
            return True

rl = RateLimiter2(10, 1)
for _ in range(10):
    print(rl.call(1))
time.sleep(0.5)
for _ in range(10):
    print(rl.call(1))
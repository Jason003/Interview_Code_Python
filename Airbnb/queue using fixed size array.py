class MyQueue:
    def __init__(self, size):
        self.size = size
        self.arr = []
        self.offer_arr = self.arr
        self.poll_arr = self.arr
        self.total = 0
        self.tail = 0
        self.head = 0

    def offer(self, num):
        self.tail += 1
        self.total += 1
        if self.tail == self.size:
            self.tail = 1
            new_arr = [num]
            self.offer_arr.append(new_arr)
            self.offer_arr = new_arr
        else:
            self.offer_arr.append(num)

    def poll(self):
        if self.total <= 0:
            return
        self.total -= 1
        res = self.poll_arr[self.head]
        self.head += 1
        if self.head == self.size - 1:
            self.poll_arr = self.poll_arr[-1]
            self.head = 0
        return res

    def __str__(self):
        return str(self.arr)


queue = MyQueue(4)
for _ in range(100):
    queue.offer(_)
    print(queue)
for _ in range(100):
    print(queue.poll())
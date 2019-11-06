import heapq
class ExamRoom:
    def dist(self, x, y):
        if x == -1:
            return -y
        elif y == self.N:
            return -(self.N - x - 1)
        else:
            return -((y - x) // 2)

    def __init__(self, N: int):
        self.N = N
        self.heap = [(self.dist(-1, N), -1, N)]

    def seat(self) -> int:
        _, x, y = heapq.heappop(self.heap)
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.heap, (self.dist(x, seat), x, seat))
        heapq.heappush(self.heap, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p: int) -> None:
        tail, head = None, None
        for i in self.heap:
            if i[2] == p: head = i
            if i[1] == p: tail = i
            if head and tail: break
        self.heap.remove(head)
        self.heap.remove(tail)
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, (self.dist(head[1], tail[2]), head[1], tail[2]))


        # Your ExamRoom object will be instantiated and called as such:
        # obj = ExamRoom(N)
        # param_1 = obj.seat()
        # obj.leave(p)
import collections
class SlidingPuzzle:
    def __init__(self):
        self.dir = ((1, 0), (-1, 0), (0, 1), (0, -1))


    def _valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def _swap(self, s, a, b):
        arr = list(s)
        arr[a], arr[b] = arr[b], arr[a]
        return ''.join(arr)

    def _buildBoard(self, board):
        return ''.join(str(board[i][j]) for i in range(len(board)) for j in range(len(board[0])))

    def _moveBoard(self, curr, m, n):
        zeroIdx = curr[-1].find('0')
        x, y = zeroIdx // n, zeroIdx % n
        nxt_boards = []
        for d in self.dir:
            nxt_x, nxt_y = x + d[0], y + d[1]
            if self._valid(nxt_x, nxt_y, m, n):
                nxt_boards.append(self._swap(curr[-1], zeroIdx, nxt_x * n + nxt_y))
        return nxt_boards

    def slidingGame(self, board1, board2):
        if not board1 or not board1[0]:
            return -1
        m, n = len(board1), len(board1[0])
        start = self._buildBoard(board1)
        end = self._buildBoard(board2)
        seen = set()
        dq = collections.deque([[start]])
        step = 0
        while dq:
            sz = len(dq)
            for _ in range(sz):
                curr = dq.popleft()
                if curr[-1] == end:
                    return step + 1, curr
                for nxt in self._moveBoard(curr, m, n):
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append(curr + [nxt])
            step += 1
        return -1



board1 = [[4,1,2], [5,0,3]]
board2 = [[1,2,3], [4,5,0]]
sp = SlidingPuzzle()
print(sp.slidingGame(board1, board2))
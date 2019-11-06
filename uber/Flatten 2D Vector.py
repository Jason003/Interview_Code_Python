class Vector2D(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col, self.vec2d = 0, 0, vec2d

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.hasNext():
            self.col += 1
            return self.vec2d[self.row][self.col - 1]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.row < len(self.vec2d) and \
                        self.col >= len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)
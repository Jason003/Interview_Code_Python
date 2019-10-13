class Sector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class File:
    def __init__(self, path):
        self.path = path

    def exists(self):
        return True

    def read(self):
        return bytearray(self.path, encoding='utf-8')

    def write(self, bytes):
        pass


class Image:
    def __init__(self, bytes):
        self.bytes = bytes

    def getBytes(self):
        return self.bytes


# class SpacePanorama:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.map = {}  # key: (x, y) value: path of image
#
#     def update(self, x, y, image):
#         if x < 0 or x >= self.rows or y < 0 or y >= self.cols or (x, y) not in self.map:
#             return
#         bytes = image.getBytes()
#         path = self.map[x, y]
#         file = File(path)
#         file.write(bytes)
#
#     def fetch(self, x, y):
#         if x < 0 or x >= self.rows or y < 0 or y >= self.cols or (x, y) not in self.map:
#             return None
#         path = self.map[x, y]
#         file = File(path)
#         if not file.exists():
#             return None
#         bytes = file.read()
#         return Image(bytes)

class Node:
    def __init__(self, val):
        self.pre = None
        self.nxt = None
        self.val = val

class SpacePanorama_LRU:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.basePath = ''
        self.map = {}  # key: (x, y) value: path of image

        self.head = Node(Sector(0, 0))
        self.tail = Node(Sector(0, 0))
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.key_node = {}

    def _addAfter(self, preNode, toAdd):
        nxt = preNode.nxt
        toAdd.nxt = nxt
        nxt.pre = toAdd
        toAdd.pre = preNode
        preNode.nxt = toAdd

    def _remove(self, node):
        node.pre.nxt, node.nxt.pre = node.nxt, node.pre

    def _hashImage(self, image):
        return "".join(map(lambda b: format(b, "02x"), image.getBytes()))


    def update(self, sector, image):
        if sector.x < 0 or sector.x >= self.rows or sector.y < 0 or sector.y >= self.cols or sector not in self.map:
            return
        bytes = image.getBytes()
        path = self.basePath + self._hashImage(image)
        file = File(path)
        file.write(bytes)

        if sector not in self.key_node:
            self.key_node[sector] = Node(sector)
        node = self.key_node[sector]
        self._remove(node)
        self._addAfter(self.head, node)


    def fetch(self, sector):
        if sector.x < 0 or sector.x >= self.rows or sector.y < 0 or sector.y >= self.cols or sector not in self.map:
            return None
        path = self.map[sector]
        file = File(path)
        if not file.exists():
            return None
        bytes = file.read()
        return Image(bytes)

    def getStalestSector(self):
        if self.head.nxt == self.tail:
            return None
        return Sector(self.tail.pre.val)
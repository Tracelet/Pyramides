import math


class Pyramid:
    def __init__(self):
        self.s: str = ''
        self.Nodes: list = []
        self.N: int = 0
        self.level: list = []

    def read(self, path='input.txt'):
        with(open(path)) as f:
            self.s = f.read()
        self.N = len(self.s)

    def write(self, path='output.txt'):
        with(open(path, 'w')) as f:
            f.write(self.s)

    def extract_node(self):
        last = False
        for i in range(round(math.sqrt(self.N))):
            self.level.append(i*2+1)

        i = 0
        c = 0
        while(len(self.level) != 0):
            if i % 2 == 0:
                self.Nodes.append(self.s[2*i: i*2 + 3] + self.s[self.level[-1] + i*2])
            elif i % 2 == 1 and not last:
                self.Nodes.append(self.s[i*2 + 1] + self.s[i*2 - 1 + self.level[-1]: i*2 - 1 + 3 + self.level[-1]])
            i += 1
            if len(self.Nodes) == (self.level[-1] + self.level[-2]) / 4 + c:
                c += (self.level[-1] + self.level[-2]) / 4
                self.s = self.s[self.level[-1] + self.level[-2]:]
                self.level.remove(self.level[-1])
                self.level.remove(self.level[-1])
                i = 0
                if len(self.level) == 2:
                    last = True

    def compress(self):
        if math.log(self.N, 4) % 1 != 0:
            return
        self.extract_node()
        compressed_pyramid: str = ''
        for node in self.Nodes:
            if node.count(node[0]) == 4:
                compressed_pyramid += node[0]
            else:
                compressed_pyramid += node
        self.s = compressed_pyramid
        self.N = len(self.s)
        self.Nodes = []


if __name__ == '__main__':
    p = Pyramid()
    p.read()
    iter = int(math.log(p.N, 4) - 1)
    for i in range(iter):
        p.compress()

    p.write()


class Point:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(self.x)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def bfs(self):
        #print(self.data,queue)
        if self.data not in queue:
            print(self.data)
            queue.append(self.data)
        if self.left:
            print(self.left.data)
            queue.append(self.left.data)
        if self.right:
            print(self.right.data)
            queue.append(self.right.data)
        if self.left:
            self.left.bfs()
        if self.right:
            self.right.bfs()
        #print(self.queue)

queue = []
p = Point(1.2)
p.print()

root = Node(5)
root.insert(2)
root.insert(1)
root.insert(8)
root.insert(3)
root.insert(6)
root.insert(9)
root.insert(4)
root.bfs()

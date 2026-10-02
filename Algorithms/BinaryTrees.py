from operator import indexOf


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    def search_node(self, current, value):
        if not current:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self.search_node(current.left, value)
        if value > current.value:
            return self.search_node(current.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current, value):
        if not current:
            return current

        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            temp = self._find_min(current.right)
            current.value = temp.value
            current.right = self._delete(current.right, temp.value)
        return current

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

tree = Tree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(10)
tree.insert(25)
tree.insert(60)
tree.insert(80)
tree.insert(75)
tree.insert(85)

tree.inorder_traversal(tree.root)
print()
tree.preorder_traversal(tree.root)
print()
tree.postorder_traversal(tree.root)
print()
print(tree.search_node(tree.root, 5))
tree.delete(20)
tree.inorder_traversal(tree.root)
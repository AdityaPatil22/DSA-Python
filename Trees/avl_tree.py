"""
AVL Tree implementation

An AVL tree is a self-balancing Binary Search Tree (BST). The key idea is simple:

After every insert/delete, the tree rotates itself to stay balanced
(so operations remain O(log n)).

For every node:

balance_factor = height(left) - height(right)
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # rotation
        x.right = y
        y.left = T2

        # update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # rotation
        y.left = x
        x.right = T2

        # update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):

        # 1. Normal BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. Handle imbalance

        # LL
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


tree = AVLTree()
root = None

nums = [10, 20, 30, 40, 50, 25]

for num in nums:
    root = tree.insert(root, num)

tree.inorder(root)
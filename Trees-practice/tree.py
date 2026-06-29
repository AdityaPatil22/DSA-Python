class Treenode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)


def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
"""
A Binary Search Tree is a binary tree with an ordering property
    - Left child values < parent value
    - Right child values > parent value
    - No duplicate values (in classic BST definition)

      8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


# Traversals
# BST uses the same DFS/BFS syntax as Binary Trees, but Inorder Traversal has a special meaning

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


# Insert into BST
def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    elif val > root.val:
        root.right = insert_into_bst(root.right, val)
    return root


# Search in BST
def search_bst(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)


# Find Minimum & Maximum
def find_min(root):
    while root.left:
        root = root.left
    return root.val


def find_max(root):
    while root.right:
        root = root.right
    return root.val


def delete_node(root, key):
    if root is None:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None
        # Case 2: One child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # Case 3: Two children
        min_node = find_min_node(root.right)
        root.val = min_node.val
        root.right = delete_node(root.right, root.val)
    return root


def find_min_node(node):
    while node.left:
        node = node.left
    return node

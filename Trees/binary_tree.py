"""
A Tree is a non-linear hierarchical data structure consisting of nodes connected by edges
    Non-linear → Elements are not stored in a sequence.
    Hierarchical → One node is the root, and all other nodes are children of some node

    A         ← Root
   / \
  B   C       ← Children of A
 / \   \
D   E   F     ← Leaf nodes (no children)

A Binary Tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

Terminology:
    - Node: An element of the tree.
    - Edge: The connection between two nodes.
    - Root: The top node of the tree.
    - Leaf: A node with no children.
    - Height: The length of the longest path from the root to a leaf.
    - Depth: The length of the path from the root to a node.
    - Parent: A node that has child nodes
    - Child: A node that is a descendant of another node.
    - Subtree: A tree formed by a node and its descendants.

Properties:
    - A binary tree can be empty (no nodes).
    - Each node can have 0, 1, or 2 children.
    - The left child is always less than the parent node, and the right child is always greater than the parent node in a Binary Search Tree (BST).

Operations:
    - Insertion: Adding a new node to the tree.
    - Deletion: Removing a node from the tree.
    - Traversal: Visiting all nodes in a specific order (e.g., in-order, pre-order, post-order).
    - Searching: Finding a node with a specific value.

Types of Binary Trees:
    - General Binary Tree: Each node can have up to two children.
    - Full Binary Tree: Every node other than the leaves has two children.
    - Complete Binary Tree: All levels are fully filled except possibly the last level, which is filled from left to right.
    - Perfect Binary Tree: All internal nodes have two children and all leaves are at the same level.
    - Balanced Binary Tree: The height of the left and right subtrees of any node differ by at most one.
    - Binary Search Tree (BST): A binary tree where for each node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater.
    - AVL Tree: A self-balancing binary search tree where the difference in heights between left and right subtrees is at most one.
    - Red-Black Tree: A balanced binary search tree with an additional property that ensures the tree remains balanced during insertions and deletions.
"""


# Representing Trees in Python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Example of a Binary Tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)


# DFS Traversals (Recursive)
# Preorder (Node → Left → Right)
def preorder(node):
    if node is None:
        return
    print(node.val)      # Visit node
    preorder(node.left)
    preorder(node.right)


# Inorder (Left → Node → Right)
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


# Postorder (Left → Right → Node)
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


# DFS Traversals (Iterative)
# Preorder Iterative
def preorder_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Inorder Iterative
def inorder_iterative(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right


# BFS Traversal
def bfs(root):
    if root is None:
        return
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Common Utility Patterns

# Max Depth
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Min Depth
def min_depth(root):
    if root is None:
        return 0
    if root.left is None:
        return 1 + min_depth(root.right)
    if root.right is None:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


# Search in BST
def search_bst(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)

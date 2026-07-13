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
    - Only in a Binary Search Tree (BST) are all values in the left subtree less than the node's value, and all values in the right subtree greater. A general binary tree has no such ordering.

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

# ⭐️ Points
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
DFS Traversal Rules (Must Memorize)
            Root
           /    \
        Left   Right

Preorder  = Before children
Inorder   = Between children
Postorder = After children

| Traversal | Order               | Common Uses                   |
| --------- | ------------------- | ----------------------------- |
| Preorder  | Root → Left → Right | Copy tree, serialize          |
| Inorder   | Left → Root → Right | BST problems                  |
| Postorder | Left → Right → Root | Delete tree, height, diameter |
"""

# Universal Recursive DFS Template
def dfs(node):
    if node is None:
        return
    # Do something
    dfs(node.left)
    dfs(node.right)
    # Maybe do something here

# Preorder Traversal
# Recursive
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# Iterative 
def preorder(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Inorder Traversal
# Recursive
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Iterative
def inorder(root):
    stack = []
    curr = root

    while curr or stack:

        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.val)
        curr = curr.right

# Postorder Traversal
# Recursive
def postorder(node):
    if not node:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val)

# Iterative
def postorder(root):
    if not root:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val)

    
# Breadth First Search (Level Order)
from collections import deque

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Level Order Traversal Pattern
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Height / Max Depth
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(
        maxDepth(root.left),
        maxDepth(root.right)
    )

# Count Nodes
def count(root):
    if not root:
        return 0
    return 1 + count(root.left) + count(root.right)
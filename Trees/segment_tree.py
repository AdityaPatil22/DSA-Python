""" 
Segment Tree implementation

A Segment Tree is a binary tree used for fast range queries + updates on arrays (like sum, min, max).
Instead of recomputing every time, it stores answers for ranges and combines them.

Time complexity: O(log n) for both queries and updates
Space complexity: O(4n) for perfect binary tree
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
        
    def build(self, arr, index, left, right):
        if left == right:
            self.tree[index] = arr[left]
            return

        mid = (left + right) // 2

        self.build(arr, 2 * index + 1, left, mid)
        self.build(arr, 2 * index + 2, mid + 1, right)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]


    def query(self, index, left, right, ql, qr):
        # completely inside
        if ql <= left and right <= qr:
            return self.tree[index]

        # completely outside
        if right < ql or left > qr:
            return 0

        mid = (left + right) // 2

        return (
            self.query(2 * index + 1, left, mid, ql, qr) +
            self.query(2 * index + 2, mid + 1, right, ql, qr)
        )
    
    def update(self, index, left, right, pos, value):
        if left == right:
            self.tree[index] = value
            return

        mid = (left + right) // 2

        if pos <= mid:
            self.update(2 * index + 1, left, mid, pos, value)
        else:
            self.update(2 * index + 2, mid + 1, right, pos, value)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

"""
A heap is a special tree-based data structure with one key rule:

👉 Heap Property
Min Heap: Parent ≤ Children → smallest element always at root
Max Heap: Parent ≥ Children → largest element always at root

Heaps are complete binary trees:

Filled left to right
No gaps

Example (min heap):

        1
      /   \
     3     5
    / \   /
   7   9 8

But internally in Python, it's stored as a list:

heap = [1, 3, 5, 7, 9, 8]

Min Heap: Every parent is smaller than or equal to its children.
        2
      /   \
     5     7
    / \   /
   9  10 8

Max Heap: Every parent is greater than or equal to its children.
        20
      /    \
    15      12
   /  \    /
  7    9  4
"""

import heapq

heap = []

heapq.heappush(heap, 5)       # Push
heapq.heappush(heap, 2)
heapq.heappush(heap, 9)

print(heap)

smallest = heapq.heappop(heap) # Pop
heap[0]                        # Peek

nums = [5,1,9,3]
heapq.heapify(nums)            # Heapify

"""
Useful Functions

Largest k
heapq.nlargest(k, nums)

Smallest k
heapq.nsmallest(k, nums)

Merge sorted arrays
heapq.merge(a, b)

Push then Pop (more efficient)
heapq.heappushpop(heap, x)

Replace root
heapq.heapreplace(heap, x)
"""


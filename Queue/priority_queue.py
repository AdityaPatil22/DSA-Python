"""
A Priority Queue is a data structure that stores elements with priorities.
The elements with the highest priority are served first.

Time complexity: O(log n) for both insert and extract_max
Space complexity: O(n)
"""

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
    
    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
    

import heapq

pq = []

heapq.heappush(pq, 5)
heapq.heappush(pq, 1)
heapq.heappush(pq, 10)

print(heapq.heappop(pq))  # 1
print(heapq.heappop(pq))  # 5
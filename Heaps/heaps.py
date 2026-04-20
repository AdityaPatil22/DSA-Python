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
"""

class MinHeap:
    def __init__(self):
        self.a = []

    """Insert a new element into the Min Heap."""
    def insert(self, val):
        self.a.append(val)
        i = len(self.a) - 1
        while i > 0 and self.a[(i - 1) // 2] > self.a[i]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    """Delete a specific element from the Min Heap."""
    def delete(self, value):
        i = -1
        for j in range(len(self.a)):
            if self.a[j] == value:
               i = j
               break
        if i == -1:
            return

        self.a[i] = self.a[-1]
        self.a.pop()

        parent = (i - 1) // 2

        if i > 0 and self.a[i] < self.a[parent]:
            while i > 0 and self.a[(i - 1)//2] > self.a[i]:
                self.a[i], self.a[(i - 1)//2] = self.a[(i - 1)//2], self.a[i]
                i = (i - 1)//2
        else:
            self.minHeapify(i, len(self.a))

    """Heapify function to maintain the heap property.""" 
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.minHeapify(smallest, n)

    """Search for an element in the Min Heap."""
    def search(self, element):
        for j in self.a:
            if j == element:
                return True
        return False

    def getMin(self):
        return self.a[0] if self.a else None

    def printHeap(self):
        print("Min Heap:", self.a)

# Example Usage
if __name__ == "__main__":
    h = MinHeap()
    values = [10, 7, 11, 5, 4, 13]
    for value in values:
        h.insert(value)
    h.printHeap()
    
    h.delete(7)
    print("Heap after deleting 7:", h.a)
    
    print("Searching for 10 in heap:", "Found" if h.search(10) else "Not Found")
    print("Minimum element in heap:", h.getMin())


from heapq import heapify, heappush, heappop
heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

print("Head value of heap : "+str(heap[0]))

print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
print("\n")

element = heappop(heap)

print("The heap elements : ")
for i in heap:
    print(i, end = ' ')




from queue import PriorityQueue 
q = PriorityQueue() 

q.put(10)
q.put(20) 
q.put(5) 

print(q.get()) 
print(q.get()) 

print('Items in queue :', q.qsize()) 
print('Is queue empty :', q.empty()) 
print('Is queue full :', q.full())
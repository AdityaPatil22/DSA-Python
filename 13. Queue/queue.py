from collections import deque

# Native Queue using list (less efficient - use deque for production)
native_queue = []

native_queue.append(10)    # Enqueue
native_queue.append(20)
print(native_queue.pop(0))  # Dequeue → 10

native_queue[0]            # Peek → 20
len(native_queue) == 0    # Is empty?


# Using collections.deque (recommended)
q = deque()
q.append(10)    # Enqueue
q.append(20)
print(q.popleft())  # Dequeue → 10


# Custom queue class Implementation
class Queue:
    def __init__(self):
        self.items = {}
        self.front = 0
        self.rear = 0

    # Add item to end
    def enqueue(self, element):
        self.items[self.rear] = element
        self.rear += 1

    # Remove item from front
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.items[self.front]
        del self.items[self.front]
        self.front += 1
        return item

    # Get front item
    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    # Check if empty
    def is_empty(self):
        return self.size() == 0

    # Number of elements
    def size(self):
        return self.rear - self.front

    # Clear queue
    def clear(self):
        self.items = {}
        self.front = 0
        self.rear = 0

    # Convert to array
    def to_array(self):
        return [self.items[i] for i in range(self.front, self.rear)]


# Usage
queue = Queue()

queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)

print(queue.dequeue())   # 100
print(queue.peek())      # 200
print(queue.size())      # 2
print(queue.is_empty())  # False
print(queue.to_array())  # [200, 300]

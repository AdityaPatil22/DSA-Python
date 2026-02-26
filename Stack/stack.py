# Native Implementation using list
native_stack = []

native_stack.append(10)  # Add to top
native_stack.append(20)
print(native_stack.pop())  # Remove top → 20

native_stack[-1]          # Peek → 10
len(native_stack) == 0   # Is empty?


# Custom Stack Implementation
class Stack:
    def __init__(self):
        self.items = {}
        self.top = 0

    # Add to top
    def push(self, element):
        self.items[self.top] = element
        self.top += 1

    # Remove top element
    def pop(self):
        if self.is_empty():
            return None
        self.top -= 1
        item = self.items[self.top]
        del self.items[self.top]
        return item

    # Return top element without removing
    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.top - 1]

    # Return current size
    def size(self):
        return self.top

    # Check if empty
    def is_empty(self):
        return self.top == 0

    # Clear the stack
    def clear(self):
        self.items = {}
        self.top = 0

    # Convert to array (for debugging)
    def to_array(self):
        return list(self.items.values())


# Usage
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(stack.pop())    # 15
print(stack.peek())   # 10
print(stack.size())   # 2
print(stack.is_empty())  # False
print(stack.to_array())  # [5, 10]

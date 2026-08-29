# Node structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Circular Singly Linked List Class
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Add to end
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Point to itself
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Make it circular
        self.length += 1

    # Add at start
    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Update tail to point to new head
        self.length += 1

    # Remove first
    def shift(self):
        if self.head is None:
            return None

        removed = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.length -= 1
        return removed

    # Remove last
    def pop(self):
        if self.head is None:
            return None

        removed = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
        self.length -= 1
        return removed

    # Print list (with safety to avoid infinite loop)
    def to_array(self):
        result = []
        if self.head is None:
            return result

        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break

        return result

    # Check if list contains a value
    def contains(self, value):
        if self.head is None:
            return False

        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break

        return False


# Usage
list_obj = CircularLinkedList()

list_obj.push(10)
list_obj.push(20)
list_obj.push(30)
print(list_obj.to_array())  # [10, 20, 30]

list_obj.unshift(5)
print(list_obj.to_array())  # [5, 10, 20, 30]

list_obj.pop()     # removes 30
list_obj.shift()   # removes 5

print(list_obj.to_array())  # [10, 20]
print(list_obj.contains(20))  # True
print(list_obj.contains(99))  # False

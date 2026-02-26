# Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Singly Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Add at end
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Remove last
    def pop(self):
        if self.head is None:
            return None

        current = self.head
        new_tail = current

        while current.next:
            new_tail = current
            current = current.next

        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None

        return current

    # Add at start
    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Remove first
    def shift(self):
        if self.head is None:
            return None

        removed = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return removed

    # Get node by index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        count = 0

        while count < index:
            current = current.next
            count += 1

        return current

    # Set value at index
    def set(self, index, value):
        node = self.get(index)
        if node is None:
            return False
        node.value = value
        return True

    # Insert at index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.unshift(value)
            return True
        if index == self.length:
            self.push(value)
            return True

        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    # Remove at index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        removed = prev.next
        prev.next = removed.next
        self.length -= 1
        return removed

    # Print list as array
    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


# Usage
list_obj = SinglyLinkedList()

list_obj.push(10)
list_obj.push(20)
list_obj.push(30)
print(list_obj.to_array())  # [10, 20, 30]

list_obj.unshift(5)
print(list_obj.to_array())  # [5, 10, 20, 30]

list_obj.pop()   # removes 30
list_obj.shift()  # removes 5

list_obj.insert(1, 15)  # insert 15 at index 1
list_obj.set(0, 100)    # set index 0 to 100
print(list_obj.to_array())  # [100, 15, 20]

list_obj.remove(1)  # removes 15
print(list_obj.to_array())  # [100, 20]


# Reversing a linked-list
def reverse_list(head):
    curr = head
    prev = None

    while curr is not None:
        # Store next
        next_node = curr.next

        # Reverse current node's next pointer
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = next_node

    return prev


# Deleting a node in a linked-list
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

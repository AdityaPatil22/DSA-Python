# Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# DoublyLinkedList Class
class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    # Remove last
    def pop(self):
        if self.tail is None:
            return None

        removed = self.tail

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = removed.prev
            self.tail.next = None
            removed.prev = None

        self.length -= 1
        return removed

    # Add at start
    def unshift(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    # Remove first
    def shift(self):
        if self.head is None:
            return None

        removed = self.head

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = removed.next
            self.head.prev = None
            removed.next = None

        self.length -= 1
        return removed

    # Get node by index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        # Optimization: decide direction
        if index <= self.length / 2:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count += 1
        else:
            current = self.tail
            count = self.length - 1
            while count > index:
                current = current.prev
                count -= 1

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
        before = self.get(index - 1)
        after = before.next

        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node

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

        removed = self.get(index)
        before = removed.prev
        after = removed.next

        before.next = after
        after.prev = before

        removed.next = None
        removed.prev = None

        self.length -= 1
        return removed

    # Convert to array (for debugging)
    def to_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr


# Usage
list_obj = DoublyLinkedList()

list_obj.push(1)
list_obj.push(2)
list_obj.push(3)
print(list_obj.to_array())  # [1, 2, 3]

list_obj.unshift(0)
list_obj.insert(2, 1.5)
list_obj.set(3, 2.5)

print(list_obj.to_array())  # [0, 1, 1.5, 2.5, 3]

list_obj.remove(1)  # remove node with value 1
list_obj.pop()      # remove 3
list_obj.shift()    # remove 0

print(list_obj.to_array())  # [1.5, 2.5]

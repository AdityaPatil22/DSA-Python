# Node Structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Traversal

curr = head
while curr:
    print(curr.val)
    curr = curr.next

----------------------------

Reverse

prev = None
curr = head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev

----------------------------

Middle

slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

----------------------------

Cycle

slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

----------------------------

Find Middle

slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

----------------------------
    
Dummy Node
dummy = ListNode(0)

----------------------------

Remove Nth From End: Fast -> Slow -> Delete

Delete Node
node.val = node.next.val
node.next = node.next.next


Previous Pointer
prev = None
curr = head

Fast and slow pointer: slow = fast = head

----------------------------

Merge Two Sorted Lists

dummy = ListNode()
tail = dummy

----------------------------

Delete Head
head = head.next

----------------------------

Insert at Beginning

new.next = head
head = new
"""
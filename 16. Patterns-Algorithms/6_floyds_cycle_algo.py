"""
Floyd's cycle algorithm also known as the "Tortoise and Hare" algorithm, Detects if a cycle exists in a singly linked list and optionally finds the starting node of the cycle

It uses two pointers:
- slow (tortoise) → moves 1 step at a time.
- fast (hare) → moves 2 steps at a time.
"""


# Detects if a cycle exists
def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next           # move 1 step
        fast = fast.next.next      # move 2 steps

        if slow == fast:
            return True            # cycle detected

    return False                   # no cycle


# Find start of the cycle
def detect_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
            return start  # Node where cycle begins

    return None  # No cycle

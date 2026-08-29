"""
A HashSet is a collection of unique values — it doesn't allow duplicates. It supports fast operations like:
add(value)
has(value)
delete(value)
size()
values()

Time Complexity: O(1)

Adding an element
Take the element → pass it through a hash function → get a hash code.
   Example: "Aditya" → hash → 934857.
Convert the hash code to an array index using modulo (%) with the capacity.
   Example: 934857 % 16 = 9 → bucket 9.
If bucket 9 is empty → place the element there.
If bucket 9 has other elements (collision) → store in the same bucket (linked list or tree).
If the element already exists in the bucket → do nothing (maintains uniqueness).
"""

# Use Python's Built-in set
s = set()

s.add("apple")
s.add("banana")
s.add("apple")  # duplicate, won't be added

print("banana" in s)   # True
print("grape" in s)    # False

s.discard("banana")

print(len(s))          # 1
print(list(s))         # ['apple']


# Custom HashSet Class
class HashSet:
    def __init__(self, size=53):
        self.data = [None] * size

    def _hash(self, value):
        key_str = str(value)
        total = 0
        PRIME = 31
        for i in range(min(len(key_str), 100)):
            char = ord(key_str[i]) - 96
            total = (total * PRIME + char) % len(self.data)
        return total

    def add(self, value):
        index = self._hash(value)
        if self.data[index] is None:
            self.data[index] = []

        for v in self.data[index]:
            if v == value:
                return  # already exists

        self.data[index].append(value)

    def has(self, value):
        index = self._hash(value)
        bucket = self.data[index]
        if bucket:
            for v in bucket:
                if v == value:
                    return True
        return False

    def delete(self, value):
        index = self._hash(value)
        bucket = self.data[index]
        if bucket:
            try:
                i = bucket.index(value)
                bucket.pop(i)
                return True
            except ValueError:
                pass
        return False

    def values(self):
        result = []
        for bucket in self.data:
            if bucket:
                result.extend(bucket)
        return result

    def size(self):
        count = 0
        for bucket in self.data:
            if bucket:
                count += len(bucket)
        return count


# Usage
set1 = HashSet()

set1.add("apple")
set1.add("banana")
set1.add("apple")

print(set1.has("banana"))   # True
print(set1.has("grape"))    # False
print(set1.values())       # ['apple', 'banana']
print(set1.size())         # 2

set1.delete("banana")
print(set1.values())       # ['apple']

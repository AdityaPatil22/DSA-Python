"""
A HashMap is a data structure that stores key-value pairs, allowing fast insertion, deletion, and lookup (typically O(1))
Time complexity:
- Best: O(1)
- Worst: O(n)

pre storing and then fetching

The Process of Storing a Key-Value Pair
Step 1: Hashing the key
   A hash function takes your key and turns it into a fixed-size integer (hash code).
   Example: "name" → 43248293

Step 2: Finding the bucket
   The hash code is converted into an array index (usually via % array_length).
   Example: 43248293 % 16 = 5 → put it in bucket 5.

Step 3: Handling collisions
   Different keys can end up in the same bucket. This is called a collision.
   Common solutions:
       Separate Chaining → each bucket is a linked list or tree that stores all colliding entries.
       Open Addressing → find the next empty spot in the array.

The Process of Retrieving a Value
   Take the key you want.
   Hash it again → find the bucket.
   Search inside the bucket for the exact key (needed in case of collisions).
   Return the value
"""

# Python built-in dict (similar to Map)
m = {}

m["apple"] = 5
m["banana"] = 10

print(m.get("apple"))    # 5
print("banana" in m)     # True
print(len(m))            # 2

del m["apple"]
print("apple" in m)      # False

# Iterate
for key, value in m.items():
    print(key, value)


# HashMap Class
def _hash(key, length):
    """Hash function for keys"""
    key_str = str(key)
    total = 0
    PRIME = 31
    for i in range(min(len(key_str), 100)):
        char = ord(key_str[i]) - 96
        total = (total * PRIME + char) % length
    return total


class HashMap:
    def __init__(self, size=53):
        self.key_map = [None] * size

    def _hash_key(self, key):
        return _hash(key, len(self.key_map))

    def set(self, key, value):
        index = self._hash_key(key)
        if self.key_map[index] is None:
            self.key_map[index] = []

        # Update if key already exists
        for pair in self.key_map[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.key_map[index].append([key, value])

    def get(self, key):
        index = self._hash_key(key)
        bucket = self.key_map[index]
        if bucket:
            for pair in bucket:
                if pair[0] == key:
                    return pair[1]
        return None

    def has(self, key):
        return self.get(key) is not None

    def delete(self, key):
        index = self._hash_key(key)
        bucket = self.key_map[index]
        if bucket:
            for i, pair in enumerate(bucket):
                if pair[0] == key:
                    bucket.pop(i)
                    return True
        return False

    def keys(self):
        keys_arr = []
        for bucket in self.key_map:
            if bucket:
                for pair in bucket:
                    keys_arr.append(pair[0])
        return keys_arr

    def values(self):
        values_arr = []
        seen = set()
        for bucket in self.key_map:
            if bucket:
                for pair in bucket:
                    if pair[1] not in seen:
                        seen.add(pair[1])
                        values_arr.append(pair[1])
        return values_arr


# Usage
map_obj = HashMap()

map_obj.set("apple", 5)
map_obj.set("banana", 10)
map_obj.set("orange", 15)

print(map_obj.get("apple"))      # 5
print(map_obj.get("banana"))     # 10
print(map_obj.has("banana"))     # True
print(map_obj.keys())            # ['apple', 'banana', 'orange']
print(map_obj.values())          # [5, 10, 15]

map_obj.delete("banana")
print(map_obj.get("banana"))     # None

# Frequency of an element using HashMap
# map1 = {}
# for i in nums1:
#     map1[i] = map1.get(i, 0) + 1

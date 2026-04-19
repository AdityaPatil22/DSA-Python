"""
### 29. Single Number

**Question:**
Find the element that appears once.

**Input:**
[4,1,2,1,2]
**Output:**
4
"""

def single_number(nums):
    map = {}

    for i in nums:
        map[i] = map.get(i, 0) + 1
    for key in map:
        if map.get(key) == 1:
            return key
        
    return -1
        

print(single_number([4,1,2,1,2]))
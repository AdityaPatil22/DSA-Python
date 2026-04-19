"""
### 30. Missing Number

**Question:**
Find missing number from range [0,n].

**Input:**
[3,0,1]
**Output:**
2
"""

def missing_num(nums):
    nums.sort()
    for i in range(0, len(nums)):
        if i != nums[i]:
            return i

print(missing_num([3,0,1]))
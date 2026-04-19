"""

### 28. Majority Element

**Question:**
Find element appearing more than n/2 times.

**Input:**
[3,2,3]
**Output:**
3
"""
import math

def majority_element(nums):
    nums.sort()
    half = math.floor(len(nums) / 2)
    return nums[half]

print(majority_element([3,2,3]))
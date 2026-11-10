"""
Why Use a Monotonic Stack?
It helps you efficiently find:
Next Greater Element (NGE)
Next Smaller Element
Previous Greater / Smaller
Range contributions (area, spans, max/min ranges)
All in O(n) time.
"""

# Next Greater Element (NGE)
def next_greater_element(nums):
    stack = []
    result = []
    for i in range(len(nums)):
        while stack and stack[-1] < nums[i]:
            result.append(nums[i])
    return result


# Next Smaller Element
def next_smaller_element(nums):
    stack = []
    result = []
    for i in range(len(nums)):
        while stack and stack[-1] > nums[i]:
            result.append(nums[i])

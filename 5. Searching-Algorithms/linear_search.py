"""
Time Complexity:
Best Case: O(1) → if target is at the beginning
Worst Case: O(n) → if target is at the end or not present
"""

# Native Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return index where target is found
    return -1  # not found

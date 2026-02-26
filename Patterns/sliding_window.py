"""
Sliding window is used when you're dealing with:
Subarrays / substrings
Continuous elements
A window that expands or shrinks while moving forward

Time complexity: O(n)
Space complexity: O(1)
"""

# There are two main types. This distinction is SUPER important.
# 1. Fixed size window
# 2. Variable size window

# Fixed size window
def max_subarray_sum(nums, k):
    window_sum = 0
    max_sum = 0

    # first window
    for i in range(k):
        window_sum += nums[i]
    max_sum = window_sum

    # slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i]        # add right
        window_sum -= nums[i - k]    # remove left
        max_sum = max(max_sum, window_sum)

    return max_sum


# Variable size window
def longest_subarray(nums, k):
    left = 0
    total = 0
    max_len = 0

    for right in range(len(nums)):
        total += nums[right]

        while total > k:
            total -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Right pointer expands the window
# Left pointer fixes the window

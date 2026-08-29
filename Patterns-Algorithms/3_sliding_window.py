"""
It involves creating a window (a subset of the array or string) that slides over the input
to examine different parts—often maintaining some property like sum, length, or count

Use it when: You're asked to find subarrays/substrings of a certain length or condition
Types of Sliding Window: Fixed-size Window and Variable size window

Time complexity: O(n) or O(n + m)
"""

# Fixed size sliding window
def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0

    # Calculate sum of first window
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # add next, remove first
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9


# Variable size sliding window
def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.discard(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")


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


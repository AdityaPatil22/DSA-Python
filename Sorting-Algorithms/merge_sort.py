"""
Merge Sort is a classic divide and conquer algorithm:
Divide the array into halves recursively.
Sort each half.
Merge the sorted halves.

Time complexity: O(n log n)
Space complexity: O(n)
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # Add remaining elements
    result.extend(left[l:])
    result.extend(right[r:])
    return result

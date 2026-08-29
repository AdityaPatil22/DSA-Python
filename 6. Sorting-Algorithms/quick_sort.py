"""
Quick Sort is a highly efficient, divide-and-conquer sorting algorithm. It works by:
Picking a "pivot" element.
Partitioning the array: elements less than the pivot go to the left, greater go to the right.
Recursively sorting left and right parts

Time Complexity:
- Best: O(n log n)
- Worst: O(n²)

Space Complexity: O(log n)
"""


def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot
    return i + 1


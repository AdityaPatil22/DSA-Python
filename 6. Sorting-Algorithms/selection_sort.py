"""
Selection Sort works by repeatedly finding the minimum element from the unsorted part of the array
and swapping it with the first unsorted element.

Time Complexity: O(n²)
Space Complexity: O(1)
"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap if a smaller element was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



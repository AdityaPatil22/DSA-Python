"""
Bubble Sort is a simple comparison-based sorting algorithm.
It repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.
The largest values "bubble up" to the end

Time Complexity:
- Best: O(n)
- Worst: O(n²)
Space Complexity
- O(1)
"""


def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                # Swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        n -= 1  # Reduce range after each pass

    return arr

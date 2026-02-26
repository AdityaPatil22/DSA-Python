"""
Big-O of built-in methods
  append/pop: O(1)
  insert/remove/slice: O(n)
  map/filter/reduce: O(n)
Use cases: Contiguous memory storage, quick lookups by index, stack (append/pop), queue (pop(0)/append).
"""

arr = [1, 2, 3, 4]

# Common list methods
arr.append(5)       # Add to end → [1,2,3,4,5]
arr.pop()          # Remove last → [1,2,3,4]
arr.insert(0, 0)   # Add to start → [0,1,2,3,4]
arr.pop(0)         # Remove first → [1,2,3,4]
arr.pop(2)         # Remove element at index 2 → [1,2,4]
arr[1:3]           # Copy from index 1 to 2 → [2,4]
arr.index(2)       # Find index of value 2 → 1
4 in arr           # Check if value exists → True
arr.reverse()      # Reverse the list
arr.sort(key=lambda x: x)  # Sort
[x * 2 for x in arr]       # Create new list with doubled values
[x for x in arr if x > 2]  # Filter values
sum(arr)           # Sum of all

# Transversing an array using while loop
array = []
i = 0
while i < len(array):
    print(arr[i])
    i += 1

# Sum of all elements of an array
sum(arr)

# Rotating an array by k positions
def rotate(nums, k):
    """
    reverse the array
    reverse the elements uptil k
    reverse the remaining elements
    """
    k %= len(nums)

    def reverse(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    reverse(0, len(nums) - 1)  # reverse <--<------
    reverse(0, k - 1)          # reverse first part ---><----
    reverse(k, len(nums) - 1)  # reverse second part --->----->

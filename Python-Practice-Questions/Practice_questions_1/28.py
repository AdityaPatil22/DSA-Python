# Rotate a list by k positions.

nums = [1, 2, 4, 5, 6]
k = 3

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

    return nums

print(rotate(nums, k))


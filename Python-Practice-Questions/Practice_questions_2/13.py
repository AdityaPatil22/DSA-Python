# Rotate a list by K positions.

def rotateList(nums, k):
    if not nums: return nums
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotateList([1, 2, 3, 4, 5, 6], 3))
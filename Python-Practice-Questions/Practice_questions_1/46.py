# Tow Sum
def two_sum(nums, target):
    map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in map:
            return [map[complement], i]
        map[nums[i]] = i
    return -1

print(two_sum([2, 7, 11, 15], 9))

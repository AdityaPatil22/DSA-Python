# A prefix sum array stores the cumulative sum of elements up to each index.
# It is used to answer range queries efficiently.

# Example:
# Input: [1, 2, 3, 4, 5]
# Prefix sum array: [1, 3, 6, 10, 15]

# Time complexity: O(1)
# Space complexity: O(n)

nums = [2, 4, 1, 3]
prefix = []

prefix.append(nums[0])
for i in range(1, len(nums)):
    prefix.append(prefix[i - 1] + nums[i])

print(prefix)  # [2, 6, 7, 10]


# Range Sum Query Example
# Sum from index l = 1 to r = 3

def range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l - 1]


range_sum(prefix, 1, 3)  # 8 (4 + 1 + 3)

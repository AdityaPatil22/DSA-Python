# Count the frequency of each character in a string

map = {}
nums = [1, 2, 3, 4, 3, 4]
# for i in nums1:
#     map1[i] = map1.get(i, 0) + 1

for i in nums:
    map[i] = map.get(i, 0) + 1

print(map)
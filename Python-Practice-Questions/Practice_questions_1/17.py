# Count frequency of elements in a list.
arr = [1,2,3,2,3,4,5]
map = {}

for i in arr[::1]:
    map[i] = map.get(i, 0) + 1

print(map)

# Count occurrences of each character in a string.

str = "aditya"
map = {}

for i in str:
    map[i] = map.get(i, 0) + 1

print(map)
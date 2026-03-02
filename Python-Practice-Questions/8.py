# Remove duplicates from a list.

arr = [1, 2, 3, 7, 2, 5]
set = set()
for i in arr[::1]:
    set.add(i)

print(set)

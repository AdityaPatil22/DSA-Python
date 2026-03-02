# Find the largest number in a list.

arr = [1, 2, 3, 7, 2, 5]
max = 0
for i in arr[::1]:
    if i > max:
        max = i

print(max)
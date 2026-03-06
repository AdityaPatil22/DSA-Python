# Move all zeros to the end of the list.

arr = [1, 0 , 2, 0 , 0 , 3]
left = 0
right = len(arr) - 1

while left < right:
    if arr[left] != 0 and arr[right] != 0:
        left += 1
    elif arr[left] == 0 and arr[right] == 0:
        right -= 1
    elif arr[left] == 0 and arr[right] != 0:
        arr[left] , arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    elif arr[left] != 0 and arr[right] == 0:
        left += 1

print(arr)

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print(arr)
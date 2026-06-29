# Find second largest element in a list.

arr = [1, 2,3,4,5]
max = 0
second_max = 0
for i in range(0, len(arr) + 1):
    # if i > second_max and count != 2:
    #     second_max = arr[i]
    #     count += 1

    if i > max:
        second_max = max
        max = i
    elif i > second_max and i != max:
        second_max = i

print(second_max)
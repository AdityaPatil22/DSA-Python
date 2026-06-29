# Find the second largest number in a list.

numbers = [1, 2, 3, 4, 5, 30, 2]
maximum = float('-inf')
second_max = float('-inf')

for num in numbers:
    if num > maximum:
        second_max = maximum
        maximum = num
    elif maximum > num > second_max:
        second_max = num

print(second_max)
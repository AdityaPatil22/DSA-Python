# Find the largest number in a list

numbers = [1, 2, 3, 4, 5, 30, 2]
max = float('-inf')
for i in numbers:
    if i > max:
        max = i

print(max)
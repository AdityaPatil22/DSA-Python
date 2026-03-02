# Flatten a nested list.

lst = [[1, 2], [3, 4], [5, 6]]

flat = []

for sub in lst:
    for item in sub:
        flat.append(item)

print(flat)
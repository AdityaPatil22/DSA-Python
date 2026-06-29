# Merge two sorted lists.

a = [1, 3, 5]
b = [2, 4, 6]

i, j, c = 0, 0, []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c.extend(a[i:])
c.extend(b[j:])
print(c)

c = sorted(a + b)
print(c)
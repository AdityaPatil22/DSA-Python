# Print Fibonacci sequence up to n terms.

n = 10
a = 0
b = 1
for i in range(1, n + 1):
    print(a)
    sum = a + b
    a = b
    b = sum
    
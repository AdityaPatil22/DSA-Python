# Find factorial of a number (iterative + recursive).

# iteratively
n = 5
fact = 1
while n != 1:
    fact *= n
    n -= 1

print(fact)


# Recursively
def recursion(n):
    fact = 1
    fact *= n
    n -= 1
    print(n)
recursion(5)

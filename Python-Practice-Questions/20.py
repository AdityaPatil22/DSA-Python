# Check if a number is Armstrong number
import math

n = 153
original = n
total = 0

while n != 0:
    digit = n % 10
    total += math.pow(digit, 3)
    n = n // 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")


n = 153
original = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10

print("Armstrong" if total == original else "Not Armstrong")
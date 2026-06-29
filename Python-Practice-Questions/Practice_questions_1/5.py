# Check if a number is prime.

n = 13
count = 0
for i in range(1, n + 1):
    temp = n % i
    if temp == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")
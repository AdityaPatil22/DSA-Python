# Return the sum of all even numbers in a list.

arr = [1,2,3,4,5,6,7,8]
sum = 0
for i in arr[::1]:
    if i % 2 == 0:
        sum += i

print(sum)
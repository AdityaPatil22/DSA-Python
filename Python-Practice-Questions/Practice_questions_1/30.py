# Find missing number in a range 1 to n.
arr = [1,2,3,5,6,7,8,9]

n = len(arr) + 1

expected_sum = n * (n + 1) // 2

arr_sum = 0
for i in arr:
    arr_sum += i

print(expected_sum - arr_sum)
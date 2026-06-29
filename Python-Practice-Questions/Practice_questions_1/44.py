# Remove duplicates from sorted array.

arr = [1,2,3,4,4,5,5,6]
rm_dp = set()

for i in arr:
    rm_dp.add(i)

print(rm_dp)
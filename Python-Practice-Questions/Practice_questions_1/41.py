# Two sum problem.
arr = [1,2,3,4,5,7]
target = 9
map = {}
for i in range(len(arr)):
    complement = target - arr[i]

    if complement in map:
        print(map[complement], i)
        break

    map[arr[i]] = i
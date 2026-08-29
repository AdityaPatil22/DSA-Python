# Creating a 2D array
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access
print(arr[0][0])  # 1
print(arr[2][1])  # 8

# Dimensions
rows = len(arr)        # number of rows
cols = len(arr[0])     # number of columns


# Row-wise Traversal
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j])

# Column-wise Traversal
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j])

# Diagonal Traversal
for d in range(len(arr) + len(arr[0]) - 1):
    for i in range(len(arr)):
        j = d - i
        if 0 <= j < len(arr[0]):
            print(arr[i][j])

# Flattening a 2D array
flat_array = [item for sublist in arr for item in sublist]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Search in 2D Array
def search2d(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return [i, j]
    return [-1, -1]


# Sum of Rows / Columns
# Row sum
for i in range(len(arr)):
    total = 0
    for j in range(len(arr[0])):
        total += arr[i][j]
    print("Row", i, "sum:", total)

# Column sum
for j in range(len(arr[0])):
    total = 0
    for i in range(len(arr)):
        total += arr[i][j]
    print("Col", j, "sum:", total)


# Transpose of Matrix
def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result

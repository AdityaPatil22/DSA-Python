"""
Matrix traversal = visiting every cell in a 2D grid in a specific order while respecting boundaries.
Think of a matrix as:
rows → i
columns → j
"""

# Example matrix (replace with your matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Basic Matrix Traversal (Row-wise)
# Left → Right, Top → Bottom
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])

# Column-wise Traversal
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j])

# Diagonal Traversal
for d in range(len(matrix) + len(matrix[0]) - 1):
    for i in range(len(matrix)):
        j = d - i
        if 0 <= j < len(matrix[0]):
            print(matrix[i][j])

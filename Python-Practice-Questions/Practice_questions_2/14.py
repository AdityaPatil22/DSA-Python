# def star_pattern():
#     for i in range(5):
#         for j in range(5):
#             print("*", end="")
#         print()

# print(star_pattern())

# def star_pattern():
#     n = 1
#     for i in range(5):
#         for j in range(n):
#             print("*", end="")
#         n+=1
#         print()

# print(star_pattern())

# def star_pattern():
#     n = 1
#     for i in range(5):
#         for j in range(1, n):
#             print(j, end="")
#         n+=1
#         print()

# print(star_pattern())

# def star_pattern():
#     n = 1
#     for i in range(5):
#         for j in range(n):
#             print(n, end="")
#         n+=1
#         print()

# print(star_pattern())

# def star_pattern():
#     n = 5
#     for i in range(n):
#         for j in range(n):
#             print("*", end="")
#         n-=1
#         print()

# print(star_pattern())

# def star_pattern():
#     n = 5
#     for i in range(5):
#         for j in range(1, n):
#             print(j, end="")
#         n-=1
#         print()

# print(star_pattern())

# def star_pattern():
#     N = 5
#     for i in range(N):
#             # Print leading spaces
#             for j in range(N - i - 1):
#                 print(" ", end="")
#             # Print stars
#             for j in range(2 * i + 1):
#                 print("*", end="")
#             # Print trailing spaces
#             for j in range(N - i - 1):
#                 print(" ", end="")
#             # Move to next row
#             print()


# print(star_pattern())

# def star_pattern():
#     N = 5
#     for i in range(N):
#         # Print leading spaces
#         for j in range(N - i - 1):
#             print(" ", end="")

#         # Print stars
#         for j in range(2 * N - (2 * i + 1)):
#             print("*", end="")

#         # Print trailing spaces
#         for j in range(N - i - 1):
#             print(" ", end="")

#         print()

# star_pattern()

def star_pattern():
    for i in range(5):
        # If the row index is even, start with 1
        if i % 2 == 0:
            start = 1
        else:
            start = 0

        # Loop to print alternating 1's and 0's
        for j in range(i + 1):
            print(start, end="")
            # Alternate between 1 and 0
            start = 1 - start
            
        print()

print(star_pattern())
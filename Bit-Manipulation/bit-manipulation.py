# Bit Manipulation
# Integers are stored in binary (base-2)
# Each bit represents a power of 2

# 13 = 1 1 0 1
#      ↑ ↑ ↑ ↑
#      8 4 2 1


# Bitwise Operators

# Operator	   Symbol	Meaning
# AND	         &	    1 if both bits are 1
# OR	         |	    1 if either bit is 1
# XOR	         ^	    1 if bits are different
# NOT	         ~	    Flips bits
# Left Shift	 <<	    Multiply by 2
# Right Shift	 >>	    Divide by 2

# Example
5 & 3   # 1
5 | 3   # 7
5 ^ 3   # 6


# Core Bit Tricks

# Check if a bit is set
# (num & (1 << i)) != 0

# Set a bit
# num | (1 << i)

# Clear a bit
# num & ~(1 << i)

# Toggle a bit
# num ^ (1 << i)

# Check if number is even or odd
# num & 1

# Multiply / Divide by 2
# num << 1   # multiply by 2
# num >> 1   # divide by 2

# XOR Properties (EXTREMELY IMPORTANT)

# | Property           | Meaning              |
# | ------------------ | -------------------- |
# | `a ^ a = 0`        | Same numbers cancel  |
# | `a ^ 0 = a`        | Identity             |
# | XOR is commutative | Order doesn't matter |

# Find the unique element
ans = 0
for num in arr:
    ans ^= num

# Power-of-Two & Bit Counting
# (n & (n - 1)) == 0

# Generate all subsets (Power Set)
# for mask in range(1 << n):
#     for i in range(n):
#         if mask & (1 << i):
#             # element i is included
#             pass

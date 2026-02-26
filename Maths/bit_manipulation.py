"""
A bit is either 0 or 1. Numbers in computers are stored in binary form, and bitwise operations
In Python:
    Integers can be arbitrarily large
    Bitwise operations work on the binary representation
    For negative numbers, Python uses two's complement with arbitrary precision

Bitwise Operators in Python
Operator	            Symbol
AND                     &
OR	                    |
XOR	                    ^
NOT	                    ~
Left Shift	            <<
Right Shift	            >>

Common Number Systems for Programming

System	    Base	Digits used	  Example
Binary	    2	    0, 1	      1011₂ = 11₁₀
Octal	    8	    0–7	          17₈ = 15₁₀
Decimal	    10	    0–9	          59₁₀
Hexadecimal	16	    0–9, A–F      2A₁₆ = 42₁₀
"""

print(5 & 3)   # 1  (0101 & 0011 = 0001)
print(5 | 3)   # 7  (0101 | 0011 = 0111)
print(5 ^ 3)   # 6  (0101 ^ 0011 = 0110)
print(~5)      # -6 (~0101 = 1010 + sign flip)
print(5 << 1)  # 10
print(5 >> 1)  # 2
print(-5 >> 1) # -3
# Python doesn't have >>> (unsigned right shift), use: (n % (1 << 32)) >> 1 for 32-bit


# 3.1 Check if a number is even/odd
n = 5  # example
if n & 1:
    print("odd")
else:
    print("even")


# 3.2 Multiply/Divide by powers of 2
# n << k  # multiply by 2^k
# n >> k  # divide by 2^k (signed)


# 3.3 Swap two numbers without temp
# a = a ^ b
# b = a ^ b
# a = a ^ b


# 3.4 Check if k-th bit is set
# if n & (1 << k): print("bit is 1")


# 3.5 Set k-th bit
# n = n | (1 << k)


# 3.6 Clear k-th bit
# n = n & ~(1 << k)


# 3.7 Toggle k-th bit
# n = n ^ (1 << k)


# 3.8 Count set bits (Brian Kernighan's algo)
n = 13  # example
count = 0
while n > 0:
    n &= (n - 1)
    count += 1


# 3.9 Check power of two
# (n > 0) and ((n & (n - 1)) == 0)


# 3.10 XOR for finding unique element If every element appears twice except one:
arr = [2, 2, 3, 3, 5]  # example - 5 is unique
res = 0
for x in arr:
    res ^= x

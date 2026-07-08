import math

math.e           # Euler's number (~2.718)
math.log(10)     # Natural log of 10 (~2.302)
math.log(2)      # Natural log of 2 (~0.693)
math.log10(math.e)   # Base-10 log of E (~0.434)
math.log2(math.e)   # Base-2 log of E (~1.442)
math.pi          # Pi (~3.14159)
math.sqrt(0.5)   # Square root of 1/2 (~0.707)
math.sqrt(2)     # Square root of 2 (~1.414)

x = 0  # example variable
math.fabs(x)     # Absolute value of x
# Sign: (x > 0) - (x < 0) or math.copysign(1, x)
math.trunc(x)    # Integer part of x (removes fraction)
# clz32 equivalent: 32 - x.bit_length() for integers
# imul: (a * b) & 0xFFFFFFFF for 32-bit
# fround: float(x) for single precision

round(x)         # Round to nearest integer
math.floor(x)    # Round down to integer
math.ceil(x)     # Round up to integer

math.pow(b, e)   # b raised to the power e
math.sqrt(x)     # Square root of x
x ** (1/3)       # Cube root of x
math.hypot(*n)   # √(sum of squares of n numbers)

import random
random.random()  # Random number in [0, 1)
max(*n)         # Largest of given numbers
min(*n)         # Smallest of given numbers

math.log(x)      # Natural log (base e) of x
math.log10(x)    # Base-10 log of x
math.log2(x)     # Base-2 log of x
math.log1p(x)    # ln(1 + x) (accurate for small x)

math.exp(x)      # e^x
math.expm1(x)    # e^x - 1 (accurate for small x)

math.sin(x)      # Sine of x (x in radians)
math.cos(x)      # Cosine of x (x in radians)
math.tan(x)      # Tangent of x (x in radians)
math.asin(x)     # Arcsine of x (returns radians)
math.acos(x)     # Arccosine of x (returns radians)
math.atan(x)     # Arctangent of x (returns radians)
math.atan2(y, x) # Arctangent of y/x with correct quadrant

math.sinh(x)     # Hyperbolic sine of x
math.cosh(x)     # Hyperbolic cosine of x
math.tanh(x)     # Hyperbolic tangent of x
math.asinh(x)    # Inverse hyperbolic sine of x
math.acosh(x)    # Inverse hyperbolic cosine of x
math.atanh(x)    # Inverse hyperbolic tangent of x

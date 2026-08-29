"""
Basic structure of Recursion
  def recursive_function(args):
      if base_case:
          return result  # Stop recursion
      return recursive_function(smaller_problem)

Template:
def solve(input):
    if base_case:
        return
    do_something()
    solve(smaller_input)
    undo_if_needed()
"""


# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120


# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  # 8


# Sum of array
def sum_array(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_array(arr, i + 1)


print(sum_array([1, 2, 3, 4]))  # 10


# Reverse string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))  # "olleh"


# Palindrome String
def is_palindrome(s, left=0, right=None):
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)


print(is_palindrome("racecar"))  # True

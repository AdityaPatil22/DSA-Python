def rev_string(str):
    reverse = ""
    for i in str[::-1]:
        reverse += i

def is_plaindrome(str):
    reverse = ""
    for i in str[::-1]:
        reverse += i
    
    return str == reverse

def count_vowels(str):
    vowels = ["a", "e", "i", "o", "U"]
    count = 0
    for i in str[::1]:
        if i in vowels:
            count += 1

def factorial(n):
    fact = 1
    for i in range(0, n+1):
        fact *= i

    return fact 

def fibonacci(n):
    arr = []
    a , b = 0, 1
    for _ in range(1, n+1):
        arr.append(a)
        sum = a + b
        a = b
        b = sum
    return arr

def rem_duplicate(nums):
    seen = set()
    for i in range(len(nums)):
        seen.add(i)


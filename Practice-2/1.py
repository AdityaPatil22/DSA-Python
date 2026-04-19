def reverse_string(str):
    rev_str = ""
    for i in str[::-1]:
        rev_str += i

def isPalindrome(str):
    rev_str = ""
    for i in str[::-1]:
        rev_str += i
    return rev_str == str

def count_vowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for ch in str[::1]:
        if ch in vowels:
            count += 1

    return count

def factoraial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def isPrime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2

def fibonacci(n):
    a, b = 0, 1
    arr = []
    for _ in range(n):
        arr.append(a)
        a, b = b, a + b
        
def larget_num(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum

def rem_duplicates(nums):
    seen = set()
    res = []
    for i in nums:
        if i not in seen:
            seen.add(i)
            res.append(i)
    return res

def anagrams(s1, s2):
    map1 = {}
    map2 = {}
    for i in s1:
        map1[i] = map1.get(i, 0) + 1

    for i in s2:
        map2[i] = map2.get(i, 0) + 1

    return map1 == map2

def even_sum(nums):
    total = 0
    for i in nums[::2]:
        total += i
    return total

def capital(str):
    for i in range(len(str), 0):
        if str[i+1] == " ":
            str.upper(i)
    return str

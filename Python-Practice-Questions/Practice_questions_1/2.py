#Check if a string is a palindrome.
def isPalindrome(str):
    revStr = ""
    for i in str[::-1]:
        revStr += i
    return revStr == str


print(isPalindrome("abba"))
# Check whether a string is a palindrome

str = "aabaa"
revStr = ""
for i in str[::-1]:
    revStr += i

if(str == revStr):
    print("true")
else:
    print("false")
#Check if a string is a palindrome.
str = "abbase"
revStr = ""

for i in str[::-1]:
    revStr += i

if str == revStr:
    print("True")
else:
    print("false")
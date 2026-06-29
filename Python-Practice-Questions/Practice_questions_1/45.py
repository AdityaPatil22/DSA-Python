# Valid palindrome (ignore special chars)

str = "aabaa"
rev_str = ""
for i in str[::-1]:
    rev_str += i

result = "True" if str == rev_str else "False"
print(result)
# Capitalize the first letter of every word in a sentence.

str = "this is a sentence"
result = ""

for i in range(len(str)):
    if i == 0 or str[i - 1] == " ":
        result += str[i].upper()
    else:
        result += str[i]

print(result)
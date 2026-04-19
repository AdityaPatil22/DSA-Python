# Reverse a string.

def revString(str):
    revStr = ""
    for i in str[::-1]:
        revStr += i
    return revStr

print(revString("Aditya"))
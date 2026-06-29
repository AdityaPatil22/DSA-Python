# Count vowels in a string

vowels = ["a", "e", "i", "o", "u"]
str = "ditya"
count = 0

for i in str:
    if i in vowels:
        count += 1

print(count)
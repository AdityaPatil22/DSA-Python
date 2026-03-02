# Count vowels in a string.
str = "adityaaa"
count = 0
vowels = ["a", "e", "i", "o", "u"]
for ch in str:
    if ch in vowels:
        count += 1

print(count)
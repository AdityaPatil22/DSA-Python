# Count vowels in a string.
def countVowels(str):
    vowles = ["a", "e", "i", "o", "u"]
    count = 0
    for i in str[::1]:
        if i in vowles:
            count += 1
    return count
print(countVowels("aabba"))
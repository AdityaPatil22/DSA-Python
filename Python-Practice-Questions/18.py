# Return the longest word in a sentence.

def longest_word(str):
    max_len = 0
    count = 0
    for i in str[::-1]:
        if i != " ":
            count += 1
        else:
            max_len = max(count, max_len)
            count = 0
    max_len = max(max_len, count)
    return max_len

print(longest_word("This is a sentence"))
# Find first non-repeating character in a string.

s = "aabbbc"

freq = {}

# Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
    
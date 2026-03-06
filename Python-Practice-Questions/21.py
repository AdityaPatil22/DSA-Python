# Reverse words in a sentence.
s = "this is a sentence"

words = s.split()
rev_sentence = " ".join(words[::-1])

print(rev_sentence)

# reverse characters of each word
s = "this is a sentence"

words = s.split()
rev_sentence = ""

for word in words:
    rev_sentence += word[::-1] + " "

print(rev_sentence.strip())
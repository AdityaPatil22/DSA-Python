"""
Each string is stored as an array of characters under the hood.
Strings are immutable, meaning any operation creates a new string.
String indexing is like array indexing.
"""

s = "hello world"

# Basic properties
len(s)          # 11

# Accessing characters
s[0]            # 'h'
s[1]            # 'e' (or use indexing directly)

# String manipulation
s.upper()       # "HELLO WORLD"
s.lower()       # "hello world"
s.strip()       # removes whitespace from both ends
s[0:5]          # "hello"
s[0:5]          # "hello" (slice, substring equivalent)

# Searching
s.index("o")    # 4 (raises ValueError if not found)
s.rindex("o")   # 7
"world" in s    # True
s.startswith("hel")   # True
s.endswith("ld")      # True

# Replace
s.replace("world", "Python")    # "hello Python"
s.replace("l", "X")             # "heXXo worXd" (replaces all by default)

# Split & Join
s.split(" ")    # ["hello", "world"]
" ".join(["hello", "Python"])   # "hello Python"

# Reversal
s[::-1]         # "dlrow olleh"

# Sort a string alphabetically
"".join(sorted(s))  # "dehllloorw"

"""
| Function / Method | Use Case                                                                 |
| ----------------- | ------------------------------------------------------------------------ |
| `re.search()`     | Returns match object or None → check if a string matches regex.          |
| `re.match()`      | Returns match at start of string.                                       |
| `re.findall()`    | Returns list of all matches.                                             |
| `re.finditer()`   | Returns iterator of match objects (with groups, etc.).                   |
| `re.sub()`        | Replace matches with something.                                         |
| `re.split()`      | Split string by regex pattern.                                          |
"""

import re

# Character Matching

# . → Any single character (except newline).
# [abc] → One of a, b, or c.
# [^abc] → Not a, b, or c.
# [a-z] → Lowercase letters.
# [A-Z] → Uppercase letters.
# [0-9] or \d → Digit.
# \D → Not a digit.
# \w → Word char (letters, digits, _).
# \W → Non-word char.
# \s → Whitespace.
# \S → Non-whitespace.


# Quantifiers

# a* → Zero or more a.
# a+ → One or more a.
# a? → Zero or one a.
# a{n} → Exactly n times.
# a{n,} → At least n times.
# a{n,m} → Between n and m times.
# Anchors
# ^ → Start of string.
# $ → End of string.
# \b → Word boundary.
# \B → Not a word boundary.


# Groups

# (abc) → Grouping.
# (a|b) → a or b.
# (?:abc) → Non-capturing group.
# (?P<name>abc) → Named group.
# Lookarounds (advanced, but very useful in DSA)
# (?=...) → Positive lookahead.
# (?!...) → Negative lookahead.
# (?<=...) → Positive lookbehind.
# (?<!...) → Negative lookbehind.


# Check if string is alphanumeric
bool(re.match(r'^[a-zA-Z0-9]+$', "abc123"))  # True


# Split license key string
re.split(r'-', "2-4A0r7-4k")  # ["2", "4A0r7", "4k"]


# Validate binary string
# bool(re.match(r'^[01]+$', "101010"))  # True


# Extract numbers
re.findall(r'\d+', "abc123def456")  # ["123", "456"]


# Remove all spaces
re.sub(r'\s+', "", "  hello world  ")  # "helloworld"


# Check palindrome with regex help
s = "A man, a plan, a canal: Panama"
s = re.sub(r'[^a-z0-9]', '', s.lower())
# "amanaplanacanalpanama"

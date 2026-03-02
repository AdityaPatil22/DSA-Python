# Check if two strings are anagrams.

str1 = "abc"
str2 = "bca"

if len(str1) != len(str2):
    print("false")
else:
    map1 = {}
    map2 = {}

    for i in str1:
        map1[i] = map1.get(i, 0) + 1

    for i in str2:
        map2[i] = map2.get(i, 0) + 1

    isAnagram = "true"

    for key, val in map1.items():
        if map2.get(key, 0) != val:
            isAnagram = "false"
            break

    print(isAnagram)
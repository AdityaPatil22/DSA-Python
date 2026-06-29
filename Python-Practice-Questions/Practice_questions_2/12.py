# Remove duplicates from a list.

def remDuplicate(nums):
    seen = set()
    result = []
    for i in nums:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result

print(remDuplicate([1, 2, 1, 2, 3, 4]))
# Check if two strings are rotations of each other.

def areRotations(s1, s2):
    n = len(s1)

    for _ in range(n):
        if s1 == s2:
            return True
        
        s1 = s1[-1] + s1[:-1]

    return False

if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"

    print("true" if areRotations(s1, s2) else "false")
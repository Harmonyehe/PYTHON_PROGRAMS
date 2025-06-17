def is_ana(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()

    if len(a) != len(b):
        return False

    ca = [0] * 26
    cb = [0] * 26

    for char in a:
        i = ord(char) - ord('a')
        ca[i] += 1

    for char in b:
        i = ord(char) - ord('a')
        cb[i] += 1

    if ca == cb:
        return True
    else:
        return False

# Get user input
a = input("Enter word: ")
b = input("Enter word: ")

if is_ana(a, b):
    print("✅ Is an anagram")
else:
    print("❌ Not an anagram")

import re

def is_palindrome_valid(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s).replace(' ', '').lower()
    print(s)

    for i in range(int(len(s) / 2)):
        j = len(s) - i - 1
        print(s[i], s[j])
        if s[i] != s[j]:
            return False

    return True

s = 'a dog! a panic in a pagoda.'
print(is_palindrome_valid(s))
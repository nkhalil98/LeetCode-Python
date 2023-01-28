"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""

def toLowerCase(s: str) -> str:
        word = []
        for char in s:
            if 'A'  <= char <= 'Z':
                num = ord(char)
                new_char = chr(num + 32)
                word.append(new_char)
            else:
                word.append(char)
        return ''.join(word)

if __name__ == "__main__":
    # test cases
    assert toLowerCase("Hello") == "hello"
    assert toLowerCase("here") == "here"
    assert toLowerCase("LOVELY") == "lovely"
"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""

def toLowerCase(s: str) -> str:
        return s.lower()

if __name__ == "__main__":
    # test cases
    assert toLowerCase("Hello") == "hello"
    assert toLowerCase("here") == "here"
    assert toLowerCase("LOVELY") == "lovely"
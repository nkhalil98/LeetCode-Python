"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

def areAlmostEqual(s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        diff = 0
        S1 = set()
        S2 = set()
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1
                S1.add(s1[i])
                S2.add(s2[i])
        return (diff == 2) and (S1 == S2)

if __name__ == "__main__":
    # test cases
    assert areAlmostEqual("bank", "kanb") == True
    assert areAlmostEqual("attack", "defend") == False
    assert areAlmostEqual("kelb", "kelb") == True    
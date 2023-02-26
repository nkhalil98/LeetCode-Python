"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

def isSubsequence(s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 == 0:
            return True
        if n1 > n2:
            return False
        found = 0
        for i in range(n2):
            if t[i] == s[found]:
                found += 1
            if found == n1:
                return True
        return False

if __name__ == "__main__":
    # test cases
    assert isSubsequence("abc", "ahbgdc") == True
    assert isSubsequence("axc", "bar") == False
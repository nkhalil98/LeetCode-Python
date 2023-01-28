"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

def mergeAlternately(word1: str, word2: str) -> str:
        i = 0
        j = 0
        s1 = len(word1)
        s2 = len(word2)
        merged = []
        while i < s1 and j < s2:
            merged += word1[i]
            merged += word2[j]
            i += 1
            j += 1

        if i == s1:
            return ''.join(merged) + word2[j:]
        if j == s2:
            return ''.join(merged) + word1[i:]

if __name__ == "__main__":
    # test cases
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"
"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

def isAlphabetic(s1, s2, order):
        ls1 = len(s1)
        ls2 = len(s2)
        for a in range(ls1):
            if order.index(s1[a]) > order.index(s2[a]):
                return False
            elif order.index(s1[a]) == order.index(s2[a]):
                if a == ls2 - 1:
                    if ls1 == ls2:
                        return True
                    elif ls1 > ls2:
                        return False
                    return True
            else:
                return True
        return True

def isAlienSorted(words, order):
    for a in range(len(words) - 1):
        if not isAlphabetic(words[a], words[a+1], order):
            return False
    return True

if __name__ == "__main__":
    # test cases
    assert isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
    assert isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False
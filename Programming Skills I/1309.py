"""
1309. Decrypt String from Alphabet to Integer Mapping

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

Constraints:

1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.
"""

def freqAlphabets(s: str) -> str:
        d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        i = 0
        n = len(s)
        res = []
        while i < n:
            if i + 2 < n and s[i+2] == '#':
                char = s[i:i+3]
                res.append(d[char])
                i += 3
            else:
                char = s[i]
                res.append(d[char])
                i += 1
        return ''.join(res)

if __name__ == "__main__":
    # test cases
    assert freqAlphabets("10#11#12") == "jkab"
    assert freqAlphabets("1326#") == "acz"
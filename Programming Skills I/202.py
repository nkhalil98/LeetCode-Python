"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Constraints:

1 <= n <= 2^31 - 1
"""

def isHappy(n: int) -> bool:
        memo = set()
        while True:
            n_str = str(n)
            new = 0
            for char in n_str:
                new += int(char)**2
            n = new
            if n == 1:
                break
            if n in memo:
                return False
            memo.add(n)
        return True

if __name__ == "__main__":
    # test cases
    assert isHappy(19) == True
    assert isHappy(2) == False
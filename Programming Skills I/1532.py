"""
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Constraints:

0 <= low <= high <= 10^9
"""

def countOdds(low: int, high: int) -> int:
    r = (high - low) // 2
    if low%2 == 0 and high%2 == 0:
        return r
    return r + 1

if __name__ == "__main__":
    # test cases
    assert countOdds(3,7) == 3
    assert countOdds(8, 10) == 1
    assert countOdds(1,10) == 5

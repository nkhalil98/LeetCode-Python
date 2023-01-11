"""
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

def countOdds(low: int, high: int) -> int:
    r = (high - low) // 2
    if low%2 == 0 and high%2 == 0:
        return r
    return r + 1

if __name__ == "__main__":
    print(countOdds(3,7))  # 3
    print(countOdds(8, 10)) # 1
    print(countOdds(1,10)) # 5

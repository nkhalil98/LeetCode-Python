"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Constraints:

1 <= n <= 10^5
"""

def subtractProductAndSum(n: int) -> int:
        nums = [int(char) for char in str(n)]
        total = 0
        prod = 1
        for num in nums:
            total += num
            prod *= num
        return prod - total

if __name__ == "__main__":
    # test cases
    assert subtractProductAndSum(234) == 15
    assert subtractProductAndSum(4421) == 21
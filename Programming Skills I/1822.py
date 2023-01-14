"""
1822. Sign of the Product of an Array

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""

def arraySign(nums: list[int]) -> int:
    negatives = 0
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            negatives += 1
        else:
            continue
    if negatives%2 == 1:
        return -1
    return 1

if __name__ == "__main__":
    # test cases
    assert arraySign([-1,-2,-3,-4,3,2,1]) == 1
    assert arraySign([1,5,0,2,-3]) == 0
    assert arraySign([-1,1,-1,1,-1]) == -1
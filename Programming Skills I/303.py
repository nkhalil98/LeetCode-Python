"""
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.

int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Constraints:

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.
"""

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        r = self.nums[left:right+1]
        return sum(r)

if __name__ == "__main__":
    # test cases
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    assert numArray.sumRange(0, 2) == 1
    assert numArray.sumRange(2, 5) == -1
    assert numArray.sumRange(0, 5) == -3
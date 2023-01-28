"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""

def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1

if __name__ == "__main__":
    # test cases
    nums1 = [0,1,0,3,12]
    moveZeroes(nums1)
    assert nums1 == [1,3,12,0,0]
    nums2 = [0]
    moveZeroes(nums2)
    assert nums2 == [0]

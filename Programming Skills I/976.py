"""
976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Constraints:

3 <= nums.length <= 10^4
1 <= nums[i] <= 10^6
"""

def largestPerimeter(nums: list[int]) -> int:
        nums_sorted = sorted(nums, reverse = True)
        n = len(nums_sorted)
        for num in range(n - 2):
            if nums_sorted[num] < nums_sorted[num+1] + nums_sorted[num+2]:
                return nums_sorted[num] + nums_sorted[num+1] + nums_sorted[num+2]
        return 0

if __name__ == "__main__":
    # test cases
    assert largestPerimeter([2,1,2]) == 5
    assert largestPerimeter([1,2,1,10]) == 0
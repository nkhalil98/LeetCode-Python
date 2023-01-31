"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Constraints:

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""

def isMonotonic(nums: list[int]) -> bool:
    ascending = 0
    descending = 0
    n = len(nums)
    for i in range(n-1):
        if nums[i] < nums[i+1]:
            ascending += 1
        elif nums[i] > nums[i+1]:
            descending += 1
        else:
            ascending += 1
            descending += 1
    return (ascending == n-1) or (descending == n-1)

if __name__ == "__main__":
    assert isMonotonic([1, 2, 2, 3]) == True
    assert isMonotonic([6,5,4,4]) == True
    assert isMonotonic([1,3,2]) == False
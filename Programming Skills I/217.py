"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

def containsDuplicate(nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    # test cases
    assert containsDuplicate([1,2,3,1]) == True
    assert containsDuplicate([1,2,3,4]) == False
    assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

def runningSum(nums: list[int]) -> list[int]:
        running = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            running.extend([nums[i] + running[-1]])
        return running

if __name__ == "__main__":
    # test cases
    assert runningSum([1,2,3,4]) == [1,3,6,10]
    assert runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert runningSum([3,1,2,10,1]) == [3,4,6,16,17]
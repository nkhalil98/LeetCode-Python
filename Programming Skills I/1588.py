"""
1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
 

Follow up:
Could you solve this problem in O(n) time complexity?
"""

def sumOddLengthSubarrays(arr: list[int]) -> int:
        odds = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                sub = arr[i:j]
                if len(sub)%2 == 1:
                    odds.append(sub)
        total = 0
        for odd in odds:
            total += sum(odd)
        return total

if __name__ == "__main__":
    # test cases
    assert sumOddLengthSubarrays([1,4,2,5,3]) == 58
    assert sumOddLengthSubarrays([1,2]) == 3
    assert sumOddLengthSubarrays([10,11,12]) == 66
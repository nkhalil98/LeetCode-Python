"""
496. Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        greater = []
        for num1 in nums1:
            idx = nums2.index(num1)
            is_greater = False
            for num2 in nums2[idx+1:]:
                if num2 > num1:
                    greater.append(num2)
                    is_greater = True
                    break
            if not is_greater:
                greater.append(-1)
        return greater

if __name__ == "__main__":
    # test cases
    assert nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
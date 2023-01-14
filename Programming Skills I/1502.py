"""
1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""

def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr_sorted = sorted(arr)
    diff = arr_sorted[0] - arr_sorted[1]
    n = len(arr_sorted)
    for i in range(1,n-1):
        if arr_sorted[i] - arr_sorted[i+1] != diff:
            return False
    return True

if __name__ == "__main__":
    # test cases
    assert canMakeArithmeticProgression([3, 5, 1]) == True
    assert canMakeArithmeticProgression([1, 2, 4]) == False
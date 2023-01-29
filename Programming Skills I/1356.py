"""
1356. Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""

def sortByBits(arr: list[int]) -> list[int]:
        sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))
        return sorted_arr

if __name__ == "__main__":
    # test cases
    assert sortByBits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7]
    assert sortByBits([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024]
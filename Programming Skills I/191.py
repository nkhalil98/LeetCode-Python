"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Constraints:

The input must be a binary string of length 32.
 

Follow up: If this function is called many times, how would you optimize it?
"""

def hammingWeight(n: int) -> int:
    binary = bin(n)
    return binary.count('1')
  
if __name__ == "__main__":
    # test cases
    assert hammingWeight(11) == 3
    assert hammingWeight(128) == 1
    assert hammingWeight(4294967293) == 31

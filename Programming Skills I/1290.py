"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
        decimal = []
        while head:
            decimal.append(head.val)
            head = head.next
        decimal.reverse()
        num = 0
        for i, digit in enumerate(decimal):
            num += digit * 2**i
        return num

if __name__ == "__main__":
    # test cases
    pass
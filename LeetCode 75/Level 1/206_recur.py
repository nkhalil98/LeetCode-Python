"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(self, head: ListNode) -> ListNode:
    if not head:
        return None
    new = head
    if head.next:
        new = self.reverseList(head.next)
        head.next.next = head
    head.next = None

    return new    

if __name__ == "__main__":
    # test cases
    pass
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
    new_head = None
    itr = head
    while itr:
        if not new_head:
            new_head = ListNode(itr.val, None)
        else:
            new_head = ListNode(itr.val, new_head)
        itr = itr.next
    return new_head    

if __name__ == "__main__":
    # test cases
    pass
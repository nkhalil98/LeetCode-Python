"""
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value.

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder(root: 'Node') -> list[int]:
    if not root:
        return []
    pre = [root.val]
    if root.children:
        for child in root.children:
            pre += preorder(child)
    return pre

if __name__ == "__main__":
    # test cases
    pass
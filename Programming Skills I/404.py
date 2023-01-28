"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root) -> int:
    def is_leaf(root):
        return (not root.left) and (not root.right)

    if is_leaf(root):
        return 0

    if root.left and not root.right:
        if not is_leaf(root.left):
            return sumOfLeftLeaves(root.left)
        else:
            return root.left.val

    if root.right and not root.left:
        return sumOfLeftLeaves(root.right)

    if root.right and root.left:
        if not is_leaf(root.left):
            return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
        else:
            return root.left.val + sumOfLeftLeaves(root.right)

 
if __name__ == "__main__":
    # test cases
    pass
"""
Invert Binary Tree
Easy

You are given the root of a binary tree root. Invert the binary tree and return its root.

Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100

https://neetcode.io/problems/invert-a-binary-tree/question?list=neetcode150
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        The TreeNode has value and left node and right node.
        Invert means swapping the left and the right children of every nodes in the tree.
        We have to swap each nodes.
        we have to traverse from root node to leaf node.
        """
        if not root: return None

        # you can swap easily
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


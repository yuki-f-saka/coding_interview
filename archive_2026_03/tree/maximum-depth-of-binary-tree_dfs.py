"""
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path
from the root node down to the farthest leaf node.

Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100

https://neetcode.io/problems/depth-of-binary-tree/question?list=neetcode150
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        My first thought is that we can use dfs because we have to return its depth.
        Using dfs, we can use recursive. It is made by base case and recursive case.
        You have to recall about fibonacci function. f(n) = f(n-1) + f(n-2)
        """
        # base case
        if not root:
            return 0

        # recursive case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


"""
We can solve in another way.
Using breadth first search.
"""        

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

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        We can solve in another way.
        Using breadth first search.
        You need to use a queue.
        """
        if not root:
            return 0
             
        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level
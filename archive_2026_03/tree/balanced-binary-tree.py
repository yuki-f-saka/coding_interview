"""
My explanation youtube:
https://youtu.be/zxPOs4Qh_s0?si=GoZZGssd_N9RnRi1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple(bool, int):
            # edge case
            if not node:
                return True, 0
            
            l_b, l_h = dfs(node.left)
            r_b, r_h = dfs(node.right)

            balanced = l_b and r_b and abs(l_h - r_h) <= 1
            
            return balanced, max(l_h, r_h) + 1

        return dfs(root)[0]
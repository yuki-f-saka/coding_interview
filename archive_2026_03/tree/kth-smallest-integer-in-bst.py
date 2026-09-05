"""
https://youtu.be/8lxyl4GQn98

A Binary search tree has an important characteristic.
From the current node, a left subtree nodes are less and a right subtree nodes are greater than the current node.

This problem hopes that we get kth smallest value. So we want to find ascending order list.
How to get that list?
We can traverse like this.
This tree is BST, So leftest node is smallest value.
Second smallest value is a parent node value and next is right child. next, next, next ,,,, etc.

In this traversal, we first visit the left subtree, then the parent node, and finally the right subtree.
Generally we call this is Inorder traversal.
In-order traversal is a type of DFS. 
It follows the depth-first strategy but defines a specific order: left subtree, current node, then right subtree.

So inorder traversal which means (Left - Node - Right order), this always gives values in sorted order.
When you visit nodes in that order, the output becomes sorted ascending order.

Let's jump into the code.

If we try to implement in-order traversal in Python in a straightforward way, we end up writing something like this.
At first, I memorized this pattern. 
But the real question is: why does it have to be written this way?
So let’s walk through it step by step using a diagram to understand what’s actually happening.

(walk through)

So this code is working.

Let me check time and space complexity.
T: O(N), S: O(h)

Finally this solution have to traverse every node of the tree and make the result list.
But ideally, at the moment we find kth smallest value, we want to stop travesal.

So NeetCode he walk through that way. But today is enough for me.
So someday I'll try walk through.

Thx
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            # edge case
            if not node:
                return 

            dfs(node.left)

            res.append(node.val)

            dfs(node.right)

        dfs(root)

        return res[k-1]
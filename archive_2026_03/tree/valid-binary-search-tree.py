"""
https://youtu.be/igAz12sUvoY

This tree is BST.
That answer is wrong.
Because it's really easy miss.

Every right sub tree nodes should be greater than 4.

If we use a brute-force, we have to check every left node value is less than root node value 4.
And we have to check if every right node value is greater than root node value 4.
Next every left sub tree should be less than 7 and greater than 7.
So time complexity is square time.

Then how can we verify if this tree is binary search tree?
We need to keep track of the boundaries.

Let's jump into the code.

In this case, we traverse each subtree, every path and this is not level order traversal.
So we can use DFS.

Using dfs, we can call a recursive function.

First of all, we define a recursive function and pass the current node and boundaries.
Considering edge case, if current node is empty, it is in the boundaries so that's true.
Then we verify if the current node value is in the boundaries. If it's not True, return False.

We need to pass children which means next node to the dfs function.
And we need to update the boundaries. If going left, updating right boundaries, otherwise left boundaries.
That's where DFS mainly point. 
If they satisfy the conditions, return true. So we can wrap them.

Finally we call dfs function and pass root node and negative and positive infinity.

Let me check complexity.

How about time complexity? This is typically dfs. So we traverse every node once a time.
Since we are using DFS, the call stack will be at most the height of the tree.
So the space complexity is O(h), where h is the height.

That's it.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            # edge case
            if not node:
                return True

            if not(l < node.val and node.val < r):
                return False

            return (dfs(node.left, l, node.val) and dfs(node.right, node.val, r))

        return dfs(root, float("-Inf"), float("Inf"))
            
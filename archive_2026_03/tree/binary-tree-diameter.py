"""
Diameter of Binary Tree
Easy

The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree.
The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

https://neetcode.io/problems/binary-tree-diameter/question?list=neetcode150
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Return the diameter of the tree.
        This means return the longest number of edges between two nodes.

        I'm not sure absolutely.
        If say so, we would better to think about an edge case.
        If the tree has only one node that is just a root node, the diameter is zero.
        If the tree has only two nodes that are a root node and a child node, we return one.
        If the tree has only three nodes, there are few patterns.
            1) one is parent, two are children.
            2) one is parent, one is child. And that child node has a child.
        Either cases return two as a diameter of it.

        Anyway, the diameter related to the depth of the tree, maybe.
        So I guess we might use DFS algorithm.
        """

        # edge case
        # if not (root.left and root.right):
        #     return 0

        # recursive case
        """
        Maybe we can use as follows. But I'm not sure how to use them. Give up.
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        """

"""
After asking Gemini, here is breakdown of my thought process
and how to bridge the gap to the working solution. (<- this expression is really useful for me! let me use next time!)

core concept
`diameter = left height + right height`

How to make recursive function? -> a funcion for getting height
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def getHeight(node: Optional[TreeNode]):
            if not node:
                return 0

            h_l = getHeight(node.left)
            h_r = getHeight(node.right)

            d = h_l + h_r

            self.max_d = max(self.max_d, d)

            return 1 + max(h_l, h_r)

        getHeight(root)

        return self.max_d

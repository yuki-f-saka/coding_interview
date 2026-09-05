"""
https://youtu.be/wkYv9B0Bu5w

The maximum width of the tree is n over two.
Even though it's one half n, we drop the constant and call it O(n).

breadh first search

queue

q = collections.deque([root])
We wrap the root in brackets to make it iterable for the deque.

We continue the loop as long as the queue is not empty.
Why? Because the queue holds all the nodes we haven't visited yet. 
Once the queue becomes empty, it means we’ve traversed every single level of the tree.

We use this for loop to process one level at a time.
By taking the len(q), we snapshop the number of nodes in the current level. 
This prevents us from mixing them with the children nodes we're adding for the next level.

We append the level list to our result after the for loop, because we want to group all nodes from the same level together.

We pop from the left side of the queue
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque([root])

        while q:

            level = []
            for i in range(len(q)): # len(q) is the number of current level
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)

        return res
"""
https://youtu.be/-YmaZTPVYLU?si=YKsTLg6lcBQuZ28y

--- introduction ---
Return only the values of the nodes that are visible from the right side of the tree
It means we we pick up a node value from each level.
A rightmost node we pick up in the current level.

Example 1 looks like easy because we only go to right child node and we can use DFS.
But how about there is another node here?
We have to check here too.

That's where level ordered traversal. That's why we can use BFS.

BFS use queue datasets.

--- code ---

we wrap the root in brackets to make it iterable for the deque.

we continue the loop as long as the queue is not empty.

And we have to hold rightmost node in the current level.
we define rithtMost = None

Then we need the lenght of q because it's the number of current nodes.

Then we should process every single nodes in the current level.
    In the loop of current level, we pop from the left of queue.
    and if it's not empty, updating rightMost and add children to our queue.

After the current level loop, we add rightMost value to the result list.

Finally, return res.

Let me check time complexity.
This way is common BFS, so we traverse every node. It means O(n)
How about space complexity?
We store nodes in the queue. The maximum is n over 2.
We can ignore constant. That O(N).

Let me check edge cases.
if root is empty, we skip the while loop. 

This is correct.

That's it.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque([root])

        while q: # every tree nodes loop
            rightMost = None
            lenQ = len(q)
            for i in range(lenQ): # current level loop
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)
        
        return res
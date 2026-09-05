"""
https://youtu.be/02GO69bc9m4

Before learning algorithm keep in mind it.
Let me organize the expression of greater and less.
A is Greater than x ->  x < A
A is Less than x -> x > A
A is Greater than or equal to x -> x <= A      <- A is at lease x
A is Less than or equal to x -> x >= A         <- A is at most x

No node greater than x -> x < not ->  x >=  every node in the path

A lot of guide told me that It's a good practice to ask your interviewer to eusure you understood the problem correctly.
I need to make sure I don't forget it, either.

We traversed from the root to the current node.
So we can use DFS.

This problem's key point is the current node is good if maximum node value so far in the path is less or equal to the current one.
X >= max(sofar in the path)


When we use DFS, we have to define the recursive function.
Assume that recursive function is going to return the result.
In this case, the number of good nodes.

Anyway we define the dfs function and pass the current node and maximum value so far in the path.

Edge case: current node is empty -> return 0

Then we verify if the current node is good.
If it is good, result is 1, otherwise 0.

We need to update max value so far

And That's where DFS mainly point.
we pass the next node called left child and right child and max value.
And these result is the number of good nodes from current node.

Then return res

Finally, we have to call dfs function.
We pass root and first max value is root value.

That's it.

Time: O(N)
Space: How many times should we call dfs function? It means how many times does we stack?
O(H) H height of this tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            # edge case
            if not node:
                return 0
            
            if node.val >= maxSoFar:
                res = 1
            else:
                res = 0

            maxSoFar = max(node.val, maxSoFar)

            res += dfs(node.left, maxSoFar)
            res += dfs(node.right, maxSoFar)

            return res
        
        return dfs(root, root.val)
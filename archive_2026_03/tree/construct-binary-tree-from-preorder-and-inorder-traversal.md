# Construct Binary Tree from Preorder and Inorder Traversal
[![Construct Binary Tree from Preorder and Inorder Traversal](https://img.youtube.com/vi/gZx6jMdHPpM/0.jpg)](https://youtu.be/gZx6jMdHPpM)

# Understand Match

## question
- preorder means (parent - left - right) order, right?
- inorder means (left - parent -right) order, right?
- Is there always exactly one correct answer?
    - Is the answer guaranteed to be unique?
    - Just to confirm, is the solution guaranteed to be unique, or can there be multiple valid answers?
    - Before solving it, I’d like to confirm whether the solution is guaranteed to be unique.
- If both array is empty, what should we return? Null(None)?
- Both ararys are consist of unique values?

## happy path
```
ex1.
        pre = [1,2,3], in = [2,1,3], 
        result  1
              2   3
        ex2.
        pre = [3,9,20,15,7], in = [9,3,15,20,7]
        result  3
            9      20
                 15   7
```
    
## edge case
base case
```
pre = [], in = []
return None
```

## constraints
- How long the length of inorder and preorder array?

# Plan
Preorder first value is going to be a root node.
It guranteed to be a root.

What does this in order array tell us?
Every value to the left of the 3 is going to be in the left subtree.
Every values to the right of the 3 are going to be in the right subtree.

Now we're basically done with this left subtree obviously, because there's no more nodes left in this area.
And these are reserved for the right subtree.
So we can ignore 9 and looking at how the right subtree node are arranged.
Look at preorder array, the first node is always root node. Then it's root of the right subtree.
And let's find same node in the inorder array, it's a middle position of them.
And repeating.

# Implement
In this case, we do repeating actions so we can use recursion way.
Assume that buildTree function is recursive function.
Recursive function needs a basecase, which is exit from recursion.

(base case)

First of all, preorder array first value is always root node. So we make root.
And, we can find where the same value is in inorder array. We can use index function. We call it mid.

(root, mid)

How to implement recursion? We attach the left subtree and the right subtree to the root node.
We call recursive func and pass to the preorder and inorder.
We take the same number of elements from the preorder array as the size of the left subtree we found in the inorder array.
So starting at 1, up until mid + 1. In python this mid+1 is non-inclusive.
We take the size of the left subtree.
So up until mid.
We want to pass after this sublist.
So starting at mid+1 goint until end. From inorder array is same.

(recursive mainly point)

# Review Evaluate

T: We traverse n times. The number of every node is n. And index() func takes liner time. So O(n^2)
S: The depth of recursion is going to be n that is number of nodes. So O(n)

If the length of preorder and inorder array is pretty big, this algorithm is too heavy.
So we should make another plan. But today is enough.

Thx

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # basecase
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
```
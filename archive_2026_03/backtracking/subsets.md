# Subsets

[![Subsets](https://img.youtube.com/vi/J3cYl8pEmUY/0.jpg)](https://youtu.be/J3cYl8pEmUY)

# Understand Match
## question
- Should we return also empty subsets?
- What order should we return subsets?
- Does the input array nums contain duplicates intergers?
- Are there any constraints or restriction, for example, what is the range of the input values nums?
- What should return if the input values are empty?

## happy path
nums = [1,2,3]
return [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    
## edge case
nums = [1]
return [[], [1]]

## constraints
1 <= nums.length <= 10
-10 <= nums[i] <= 10

# Plan
First we try to solve with brute-force.
How to use brute-force?
We iterate nums array again and again.
If we create a subset, we have to iterate once time.
For example, if we don't pick up 1, 2, 3. we can make an empty subset.
If we pick up 1 and don't pick up 2, 3. we can make an [1] subset.
Repeating it.

The key point is htat whether we pick up a value or not.
So how times should we iterate input array? This equals the number of subsets. It is 2 to the power of n, where n is length of the input array.

So we are goint to draw the decision tree.
Add one or not add.

# Implement
So first we have to prepare result array.
And backtracking is a specific type of DFS.
We use DFS to explore each our dicison tree until we reach the bottom.

So we use recursive function.
Then we need ending case
If index is out of bound.

Let's define subset.
If out of length of nums we add subset copy to result.

# Review Evaluate
Because in Python, lists are passed by reference. If we don't make a copy, every entry in our result list would just be a reference to the same

Space complexity is n * 2^n
Space complexity is n * 2^n

```python

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(i):
            # base case
            # ending condition
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # pick up
            # add nums[i] to subset 
            # we call dfs and pass the next input value
            subset.append(nums[i])
            dfs(i + 1)

            # Not pick up
            # remove nums[i] from subset
            # we call dfs and pass the next input value
            subset.pop()
            dfs(i + 1)
            
        # we call dfs and pass the first index
        dfs(0)
        # return res 
        return res
      
```

# Revisiting
In the previous video, we implemented this without passing subset as an argument, but we can also include it.

1. Passing as an Argument
- The function becomes more self-contained and explicit.It clearly defines what state the DFS is currently oprating on.
- It keeps the function pure in the sense that it doesn't rely on variables hidden in the outer scope.

2. Using outer scope variable
- Defining subset in the outer scope makes the function signature cleaner and more concise. We don't have to pass the same reference over and over again. 
- In this case, the DFS function modifies the shared state directory. Since Python lists are mutable, it works perfectly fine as long as we manage the append and pop operations correctly.

it’s a matter of preference. Both approaches have the same time and space complexity because they both operate on the same list reference in memory.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, subset):
            # base case
            # ending condition
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # pick up
            # add nums[i] to subset 
            # we call dfs and pass the next input value
            subset.append(nums[i])
            dfs(i + 1, subset)

            # Not pick up
            # remove nums[i] from subset
            # we call dfs and pass the next input value
            subset.pop()
            dfs(i + 1, subset)
            
        # we call dfs and pass the first index
        dfs(0, [])
        # return res 
        return res
```

Earliar we mentioned the space complexity is O(n * 2^n). But if we don't include the output list, it's O(n) because recursive depth is n at most.
If we include the output list, the output list has 2^n numbers of subset and the average size of subset is n/2 and we can ignore constant. So it's O(2^n * n)
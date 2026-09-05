# Permutations
[![Permutations](https://img.youtube.com/vi/hU8KutfT0Ow/0.jpg)](https://youtu.be/hU8KutfT0Ow)

# Understand Match
First let me clarify the problem.
- array of distinct intergers

## question
- How many intergers do nums contain at most and at least? -> 1 <= nums.length <= 6
- How range of nums[i] ? -> -10 <= nums[i] <= 10

## happy path
nums = [1, 2, 3], permutations = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

## edge case
nums = [1], permutations = [[1]]

## constraints
Earlier we asked.
So we already know.

# Plan

The Core Idea: Sub-problems
To solve the permutations of [1, 2, 3], we want to break it down into smaller sub-problems. The strategy is: 'Pick one number! And it is going to be the "fixed" element, and find all permutations of the remaining numbers.


Let's look at our input nums = [1, 2, 3]. We are going to run a loop for the length of this array. In each iteration, we'll follow three steps:

Pop the Front: "We take the first element out. Let's say we pop 1. Now, our nums becomes [2, 3]."

Solve Sub-problem: "We ask our function: 'Give me all permutations of these remaining numbers [2, 3].' This will return [[2, 3], [3, 2]]."

Attach and Collect: "We take that 1 we popped and attach it to the end of those results. So we get [[2, 3, 1], [3, 2, 1]]. We add these to our final result."

Backtrack (The Rotation): "This is the most important part. To prepare for the next choice, we append that 1 back to the end of nums. Now nums is [2, 3, 1]."

"See what happened? By popping from the front and appending to the back, we 'rotated' the list. In the next iteration of the loop, 2 will be at the front. We pop 2, solve for [3, 1], and then append 2 back. This ensures that every number gets a chance to be 'popped' and processed while maintaining the state for the next step."

-> pop 1 -> [2,3] -> append 1 -> [2,3,1]]

3. Transition to Pseudo-code
So, the logic in our code will look like this:
We'll have a Result list to store everything.

We need a Base Case: If len(nums) is 1, the only permutation is the list itself.

We'll Loop through the length of nums:
    n = nums.pop(0) (The 'Decision')
    perms = self.permute(nums) (The 'Recursion')

    for p in perms: p.append(n) (Building the result)
    
    res.extend(perms) 
    # Why are we using extend here? > Well, remember that perms is a list of lists. It contains all the permutations we found in the sub-problem.
    After adding our current number n to each of them, we want to take all those permutations and add them to our final result res.
    If we used append, it would nest the list. But by using extend, we are effectively merging these permutations into our result list one by one, keeping the list flat.

    nums.append(n) (The 'Backtrack/Reset')
    This 'pop-and-append' trick is a very clean way to do backtracking without needing a 'used' set or an extra index variable.

finally, return res


# Implement
```python
# Backtrack + subproblem
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        # Base case
        if len(nums) == 1:
            return [nums[:]] # Copy of the list
            
        for i in range(len(nums)):
            n = nums.pop(0) # Pick the first element
            perms = self.permute(nums) # Recursive call for remaining
            
            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n) # Backtrack: add the element back
            
        return res

```

# Review Evaluate
Dry Run:
Let's trace this with [1, 2]. We pop 1, call permute([2]). Base case returns [[2]]. We append 1 to get [2, 1]. Then we backtrack...

Complexity:
Time Complexity: O(n * n!) because there are n! permutations and we spend O(n) to build each one.
Space Complexity: O(n!) to store the results, and the recursion stack depth will be O(n).

Trade-offs/Alternative:
I could also use a used boolean array or a set to keep track of elements, which is also a very standard way to solve backtracking.



```
# NeetCode
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Base case: if input is empty, return a list containing an empty list
        if len(nums) == 0:
            # We don't need this base case because at least nums length is 1.
            # But this approach decrease elements of nums. So finally, length of nums reach 0.
            # This is guard clause for that.
            return [[]] 
            
        # Recursive step
        # Get all permutations of the subarray excluding the first element
        perms = self.permute(nums[1:])
        res = []
        
        # Take the first element and insert it into every possible position
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:] # Create a copy
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res    
```
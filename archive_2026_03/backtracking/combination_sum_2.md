# Combination Sum

[![Conbination sum 2](https://img.youtube.com/vi/zc-MrvWD4l0/0.jpg)](https://youtu.be/zc-MrvWD4l0)

# Understand Match
## question
- Does candidates contain duplicates interger? Yes
- Are candidates sorted? No
- If candidates are empty, what should we return? - The length of candidates is at least 1.
- If we are impossible to make any combinations, what shoud we return? For example candidates = [2], target = 5. - You should return the empty array.

## happy path
ex.1
candidates = [9,2,2,4,6,1,5], target = 8
res = [[1,2,5],[2,2,4],[2,6]]

ex.2
candidates = [1,2,3,4,5], target = 7
res = [[1,2,4], [2,5], [3,4]]

## edge case
candidates = [2], target = 5
res = []

## constraints
- Just to confirm, do we have any constraints? 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

# Plan
Let's think about this example.
candidates = [1,5,1,4], target = 7
res = [[1,1,5]]

If we try brute-force approach, the decision tree is here.
This is first step.

First idea is sorting.
If we sort the candidates, more efficiently.
We can find that we can cut the branch of the same result even if we use the diffrent index element.

Second idea is backtracking.


With brute-force time complexity is O(2^n) because every step we decide among 2 choices.
To avoid duplicates efficiency, we'll use backtracking and sorting.

# Implement
# Review Evaluate
Time Complexity: O(2^n) in the worst case, and it's the same result against brute-force approach.
However, in practice, pruning the branch makes it significantly faster because we can avoid some duplicate results.

Space Complexity: O(n) for the recursion stack and the current combination list.
Because we move on 1 index each steps. So maximum depth is going to be n.

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def dfs(i, cur, total)
            # basecase
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return

            # Take
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])

            # Not to take
            cur.pop()
            while candidates[i] == candidates[i+1] and i+1 < len(candidates):
                i += 1
            # When end the loop, for example [1,1,4,5]
            # i = 0, while condition is true. So increment
            # i = 1, while condition is false. So leave the loop.

            # then, we want to move on next index. element 4            
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
        
```
# Combination Sum

[![Conbination sum](https://img.youtube.com/vi/w_sHrTcIJRM/0.jpg)](https://youtu.be/w_sHrTcIJRM)

# Understand Match
## question
- Can I reuse the same value multiple times?
- Are we allowed to include duplicate combination in the output?
- Are there any constraints for example range of the nums and the length of nums?

## happy path
nums = [2, 5, 6, 9], target = 9
res = [[2,2,5][9]]

nums = [3,4,5], target = 16
res = [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

## edge case
- Can we find at least one result conbination?
nums = [3], target = 5
res = []

## constraints
- All of nums value are positive?

# Plan
- brute-force
    - n th  branch decision tree.
    - duplicate combination, it's not unique.
    - We don't want to find permutations, but unique combinations.
    - And time complexity is n ^ n. It's too much.

- We want to make 2 choices decision tree.

- I walk through in my video, URL is top of this file.

- Today, I try to walk through a plan to solve this problem without a script.

# Implement
# Review Evaluate

```python
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, sum):
            # basecase
            # ending path
            if sum == target:
                res.append(cur.copy())
                return 
            if i >= len(nums) or sum > target:
                return

            # Take
            cur.append(nums[i])
            dfs(i, cur, sum+nums[i])

            # Not to take
            cur.pop()
            dfs(i + 1, cur, sum)

        dfs(0, [], 0)

        return res
```
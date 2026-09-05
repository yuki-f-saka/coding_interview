# Contains Duplicate

# Understand Match
## question
- If nums are empty, what should we return?
- How many intergers does nums contain at most and at least?

## happy path
nums = [1,2,3,3] res = True

nums = [1,2,3] res = False

## edge case
nums = [] res = False

## constraints

# Plan

### Brute force
First we can use brute force approach.
We iterate each element, from index 0 to last element.
For instance, when index is 0, currrent value is 1.
We verify the current value against other each element.
So we use nested loop. If the current value match another value, we can return True.

psudocode is here
```
for i to len(nums)
    for j from i+1 to len(nums)
        if nums[i] == nums[j]:
            return True

return False
```

But this approach takes O(n^2) time complexity.
So we'd like to choose more efficient approach.

If we store previous elements we've already check, we can verify more efficiently.
So we can use hashset.

### Hashset
pseudocode is here.
```
hashset = set()
for i to len(nums)
    if nums[i] in hashset:
        return True
    hashset.append(nums[i])

return False
```
Time complexity is O(n) and space complexity is O(n) because we use a loop and we use only one hashset.
With brute force approach, the space complexity is O(1). It's really small. But time complexity is O(n^2).

Which approach is better?

If n is greater than 10^4, we should choose hash set approach.
But less than 10^4, we can choose brute force approach. It's called the "10^8 Rule"(Ten to the power of eight rule).

# Implement
```python

# brute force
def duplicateInteger(self, nums: list[int]) -> Boolean:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# hash set approach
def duplicateInteger(self, nums: list[int]) -> Boolean:
    hashset = set()

    for i in range(len(nums)):
        if nums[i] in hashset:
            return True
        hashset.add(nums[i])

    return False
```

# Review Evaluate

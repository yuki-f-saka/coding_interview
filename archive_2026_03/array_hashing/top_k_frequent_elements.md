# Top K Frequent Elements
[![Top K Frequent Elements](https://img.youtube.com/vi/W2yApVTZEXg/0.jpg)](https://youtu.be/W2yApVTZEXg)

**reference**
https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

# Understand Match

## question
- What are the constraints on nums and k?
- What should we return if the length of nums are less than k? For example nums = [1] k = 2
It's impossible. k is less and equal than the length of nums.
- If k is 0, what should we return?
It's impossible. k is greater and equal than 1.

## happy path
Let me clarify the example, it's more like, happy case.
nums = [1,2,2,3,3,3] k = 2
the most frequently elements is 3, and the second most frequently elements is 2
So we return [3,2]. The order doesn't matter.

## edge case
nums = [1] k = 1 return [1]

## constraints
1 <= k <= length of nums
-1000 <= nums[i] <= 1000
1 <= lengh of nums <= 10,000

# Plan
## BF
Count each element's frequency using a hash map, then sort the unique elements by frequency in descending order, and return the first k elements.

This is O(nlogn) approach.

## Another approach
Bucket sort approach.

1. Count frequencies — build a hash map `count` where `count[num] = frequency`
2. Build frequency buckets — create an array `freq` of size `n+1`. Put each number into `freq[its frequency]`
3. Read from right to left — iterate from index `n` down to `1`, collect numbers until we have k elements

psudocode is here
```
count = frequency map of nums
freq = array of n+1 empty lists.

for loop num in count
    freq[count[num]].append(num)

result = []
for i from n down to 1:
    for each num in freq[i]:
        result.append(num)
        if len(result) == k:
            return result
```
Time complexity is O(n) because we make one pass to count, one pass to fill buckets, and one pass to collect results — no sorting involved."

> "Space complexity is O(n)

# Implement
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

- "`count.get(n, 0)` — this is a safe way to get the current count. If n isn't in the map yet, it defaults to 0."
- "`freq = [[] for i in range(len(nums) + 1)]` — we need n+1 buckets because frequency can go from 0 to n inclusive."
- "`range(len(freq) - 1, 0, -1)` — we start from the highest possible frequency and go down. The `-1` step means we go backwards."
- "`if len(res) == k: return res` — we return early as soon as we have k elements. No need to scan the whole array."
- "We never need to sort. The bucket index itself acts as the sorted order."

# Review Evaluate
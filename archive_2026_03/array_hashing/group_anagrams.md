# Group anagrams
[![Group anagram](https://img.youtube.com/vi/6HuetpkQ7P0/0.jpg)](https://youtu.be/6HuetpkQ7P0)

**reference**
https://neetcode.io/problems/anagram-groups/question?list=neetcode150

# Understand Match
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## question
- What's the expected size of the input? Both the array length and string length? -> constaints
- Can I assume the strings contain only lowercase English letters? -> Only lowercase.
    - Are strings case-sensitive?
- Can the input array be empty? -> No at all.

## happy path
- strs = ["ai", "ia", "abc"] res = [["ai", "ia"], ["abc"]]
- strs = ["act","pots","tops","cat","stop","hat"] res = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

## edge case
- strs = ["a"] res = [["a"]]
- strs = [""] res = [[""]]

## constraints
1 <= strs.length <= 1000
0 <= strs[i].length <= 100

# Plan
## BF

In any situation, we need to wrap the sublist. we need a result list

If you don't have any idea, first we try iterate input array. yes loop.
In each iteration, we wanna check every exisiting anagram groups.
So we use nested loop and check if anagram.
if match, we add to the same anagrama group
otherwise, we create the new group and add to result list
Finally, return result list

This approach works in n^2 * klogk time complexity.
n is number of string
k is string length

In this way, we keep sorting string again and again.
we wanna sort only once.
## Another approach(Using Hashmap)
For each string, we build a count array of length 26 — one slot per letter of the alphabet. We increment the slot for each character we see. Then we convert that array to a tuple and use it as the hashmap key. All anagrams will produce exactly the same tuple, so they'll belong to the same bucket.

> "This runs in O(m * n) time, which is optimal — we touch each character exactly once."

### Excalidraw: What to draw

Draw the following:

1. **Input array**: `["eat", "tea", "tan", "ate", "nat", "bat"]` laid out horizontally
2. **Count array**: Show the 26-slot array for `"eat"`:
   - index 0 (a) = 1, index 4 (e) = 1, index 19 (t) = 1, rest = 0
   - Resulting tuple: `(1,0,0,0,1,0,...,1,0,0,0,0,0)` → key
3. **Hashmap**: Show the key-value pairs building up:
   - `(1,0,0,0,1,...,1,...) → ["eat", "tea", "ate"]`
   - `(1,0,0,0,0,...,1,1,...) → ["tan", "nat"]`
   - `(1,1,0,0,0,...,1,...) → ["bat"]`
4. **Final return**: `list(ans.values())`

psudocode is here
```
function groupAnagrams(strs):
    ans = defaultdict(list)

    for each string s in strs:
        count = array of 26 zeros

        for each character c in s:
            count[ord(c) - ord('a')] += 1

        ans[tuple(count)].append(s)

    return list(ans.values())
```

> "Time complexity is O(m * n) where m is the number of strings and n is the length of the longest string — we iterate over every character exactly once."
> "Space complexity is O(m * n) to store all strings in the hashmap."

# Implement
```python

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[stt]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
```

- "`defaultdict(list)` means we don't need to check if the key exists — it automatically initializes an empty list for new keys."
If we use just a dictionary, we are going to write 
```
key = tuple(count)

if key not in ans:
    ans[key] = []

ans[key].append(s)
```

- "`[0] * 26` gives us a fresh 26-slot array for every string. We reset it per iteration, so strings don't interfere with each other."

- "`ord(c) - ord('a')` maps 'a' to index 0, 'b' to 1, ..., 'z' to 25 — it's a compact way to index by character."

- "`tuple(count)` converts the list to a tuple because lists are not hashable and can not be used as dictionary keys

- "`list(ans.values())` collects all the grouped lists into the final output."

# Review Evaluate
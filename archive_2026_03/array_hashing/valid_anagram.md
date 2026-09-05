# Valid anagram
[![Valid anagram](https://img.youtube.com/vi/6HuetpkQ7P0/0.jpg)](https://youtu.be/6HuetpkQ7P0)

**reference**
https://neetcode.io/problems/is-anagram/question?list=neetcode150

# Understand Match
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## question
- Both length of s and t must be same, right? We need a guard clause here because if the length don't match, it's an immediate false.
    - We are not sure. Please verify.
- If both strings are empty, what should we return?
    - Please return True.
- Do both strings contain duplicate characters?
    - Yes, it's possible.

## happy path
True
ex1. s = "ai", t = "ia" return True
ex2. s = "frog", t = "grof" return True
ex3. s = "", t = "" return True

False
ex4. s = "frog", t = "grot" return False

## edge case
ex5. s = "frog", t = "grotf" return False

## constraints
- Are both strings all lower case? Do they contain upper case or special characters?
    - No, lower case only.
- How many characters both strings are at most and at least?
    - Starting at 0, up to 10^2

# Plan

## sorting
First idea is sorting.
If we sort both strings, we can verify that both strings are identical or not.
Time complexity is O(nlogn) because sort takes nlogn.
Space complexity is O(1) because we don't use memory at all.

psudocode is here
```
if length s is not equal length t:
    return False

sort s
sort t

if sorted_s == sorted_t:
    return True

return False
```

## hash table
Second idea is hash table.
If we use hash table, we can keep track of the count of characters of both strings.
Time complexity: O(n)
Space complexity: O(1)

psudocode is here
```
if length s is not equal length t:
    return False

counter_map

for char in s

    # counter_map[char] += 1 -> causing key error if you access a key that does not exist.
    counter_map[char] = counter_map.get(char, 0) + 1

for char in t
    counter_map[char] = counter_map.get(char, 0) - 1

for char in s
    if counter_map[char] != 0:
        return False
return True
```

In python we can use defaultdict or Counter, so we can write code more simply but complexity is same.

## collections.defaultdict
Using defaultdict, psudocode is here
```
if length s is not equal length t:
    return False

counter = collections.defaultdict(int)

for char in s
    counter[char] += 1

for char in t
    counter[char] -= 1

for char in s
    if counter[char] != 0:
        return False
return True
```
## collections.Counter
Using counter, psudocode is here
```
if length s is not equal length t:
    return False

counter = collections.Counter(s)

for char in t
    counter[char] -= 1

for char in s
    if counter[char] != 0:
        return False
return True
```

##  Compare hash table(Pythonic)
Also we can verify both counters.
In Python, we can compare hash tables, while cannot compare with golang.
So we have to iterate and veriry each element.
```
if length s is not equal length t:
    return False

counter_s = collections.Counter(s)
counter_t = collections.Counter(t)

if counter_s == counter_t:
    return True

return False
```


# Implement
```python



```

# Review Evaluate

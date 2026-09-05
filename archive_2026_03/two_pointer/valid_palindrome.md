# Valid Palindrome
# Understand Match
## question
- Given a string s. Is this ASCII or not? Should we concern about others for example emoji?
- Given a string s. What does this contain, uppercase and lowercase alphabet and interger?
- How should we handle spaces and non-alphabet?

## happy path
- s = "lol", true
- s = "lolo" false
- s = " l ! o ! l " true

## edge case
- s = "" true
- s = "s" true
- s = " " true

## constraints
How many characters does string s contain at least and at most? What's range?

# Plan
This is a Two Pointers problem.
We can use classic two pointer approach moving from both ends to the center.

### BF
The brute force approach would be to first clean the string.
And validate if the string is alphanumeric, convert to lower case.
Finally, we check if the cleaned string equals its reverse.

```python
clean = []
for c in s:
    if c.isalnum():
        clean.append(c.lower())

return clean == clean[::-1]
```
This works in O(n) time complexity. And Space complexity is also O(n).
It's using an extra memory. If possible, we want to work this in O(n) space complexity.
That's where two pointer moving from both right and left end to the center.

### Two pointer
```python
l, r = 0, len(s)

while l < r:
    if not s[l].isalnum():
        l += 1
        continue
    if not s[r].isalnum():
        r -= 1
        continue
    # both is alphanum
    if s[l].lower() != s[r].lower():
        return False
    l += 1
    r -= 1

return True
```

# Implement
PseudoCode is implement.
So let's review and evaluate

# Review Evaluate
Both approaches work in O(n) time complexity.
BF approach iterate the number of length of string s. O(n)
Two pointer approach iterate the half of them O(n/2). So efficient a bit.
BF is going to be use O(n) space complexity.
Two pointer is going to be O(1) space complexity.

So Two pointer approach is better.

# Reviewed by Gemini.

## Bug
My two pointer pseudocode has a bug.
`r = len(s)`
This would cause an IndexError.
So the fix : `r = len(s) - 1`

## `While` can be slightly cleaner to use inner skip non-alphanumeric.
```python
l, r = 0, len(s) - 1

while l < r:
    while l < r and > not s[l].isalnum():
        l += 1
    while l < r and > not s[r].isalnum():
        r -= 1
    # both is alphanum
    if s[l].lower() != s[r].lower():
        return False
    l += 1
    r -= 1

return True
```
# Valid Parentheses
[![Valid Parentheses](https://img.youtube.com/vi/cjpNCQ2VEH8/0.jpg)](https://youtu.be/cjpNCQ2VEH8)

# Understand Match
## question
- First of all how can we call these characters? '(', ')', '{', '}', '[' and ']'. -> parenthesis, curly brace, bracket

(	open parenthesis	
)	close parenthesis	
{	open curly brace	
}	close curly brace	
[	open square bracket	
]	close square bracket

- Does string s contain other characters? -> Nothing, '(', ')', '{', '}', '[' and ']' only.

## happy path
- s = "[]" true
- s = "([{}])" true

- s = "[[" false
- s = "([}])" false

- s = "[][]" true

## edge case
- s = "" ? -> The length of s is more than 1 character.

## constraints
1 <= s.length <= 1000

# Plan
### BF
We iterate every characters of s until s contains () or [] or {}. 
And removing the pair of every brackets.
If the string becomes empty, this is valid.
If remaining, this is invalid.

ex1.
s = "{([])}"
remove []
s = "{()}"
remove ()
s = "{}"
remove {}
s = ""
valid.

ex2.
s = "({])"
we can't remove
invalid

Every search of brackets works in O(n) because we look up each characters.
And if worst case, ((((((((())))))))).
We remove parenthesis n over 2 times. This is the number of loops.
Actually, total time complexity is n times n equal O(n^2).

Pseudocode is here.
```
while loop until s contains () or [] or {}
    replacing () with ""
    replacing [] with ""
    replacing {} with ""

if s is empty, return true
otherwise return false
```

### Another approach(Stack)
Valid parentheses must follow a last-opened, first-closed order.
I'll walk you through more simply.
Let's say "{[()]}"
1. { opened
2. [ opened
3. ( opened
4. ) closes the last opened (
5. ] closes [
6. } closes {

last-opened, first-closed
This is exactly how a stack works.

We use a stack to track opening brackets.
Whenever we see a closing bracket, we simply check whether it matches the most recent opening bracket on top of the stack.
If it matches, we remove that opening bracket.
If it doesn't match (or the stack is empty), the string is invalid.
A valid string ends with an empty stack.

pseudocode
```
create stack to store opening brackets.
we iterate every character of s.
    If it is an opening bracket, push it onto the stack.
    If it is a closing bracket:
        Check if the stack is not empty and its top matches the corresponding opening bracket.
        If yes, pop the stack.
        Otherwise, return false.

After ending the loop
    If the stack is empty, return True
    Otherwise, rerurn false
```

This approach work in liner time complexity, and liner time space complexity.

So if the length of string is bigger, we would like to use stack approch.
But if we don't want to use unnecessary memory, BF might be used.

As a result, 
either one is fine, but let's use stack approach for now.

# Implement
```python
stack = []

pair = {')':'(', '}':'{', ']':'['}
for c in s:
    # `in` can be used to confirm whether the map is contained in the value or not.
    if c == "(" or c == "{" or c == "[": # if c in map:
        stack.append(c)
        continue
    else:
        if stack and stack[-1] == pair[c]:
            stack.pop()
        else:
            return False

return stack == []

```

# Review Evaluate
# Reviewed by Gemini.

No: if c in map:
Yes: if not c in map:

Because `c in map` confirm if map keys contain character c or not.
So in this case we would like to check if this is a opening bracket or not. So we should use `if not c in map` is correct.

```python
stack = []

pair = {')':'(', '}':'{', ']':'['}
for c in s:
    # `in` can be used to confirm whether the map is contained in the value or not.
    if not c in map:
        stack.append(c)
        continue
    else:
        if stack and stack[-1] == pair[c]:
            stack.pop()
        else:
            return False

return stack == []
```

More simply coding

```python
stack = []

pair = {')':'(', '}':'{', ']':'['}
for c in s:
    # `in` can be used to confirm whether the map is contained in the value or not.
    if c in map: # c is a closing bracket
        if stack and stack[-1] == pair[c]:
            stack.pop()
        else:
            return False
    else: # c is a opening bracket
        stack.append(c)
        

return stack == []
```
# Encode and decode strings
[![Encode and decode strings](https://img.youtube.com/vi/W2yApVTZEXg/0.jpg)](https://youtu.be/W2yApVTZEXg)

**reference**
https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

# Understand
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

## Machine 1 (sender) has the function:
```
string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
```
## Machine 2 (receiver) has the function:
```
vector<string> decode(string s) {
    //... your code
    return strs;
}
```

## question
Let me clarify requirements.
**The most important question — this decides the whole approach:**
- Can the strings contain any character — like '#', '|', digits, spaces? Or is the character set limited?
*Why this matters: if the character set is limited, a simple delimiter works. If any character is possible, it doesn't — and we need a completely different approach.*

## happy path
strs = ["hello", "world"]
strs = ["hello", "world"]

## edge case
strs = [""]
strs = [""]

## constraints
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

# Match
The interviewer confirmed that strings can contain any character. That rules out the simple delimiter approach — I'll explain why in a moment. This is a serialization design problem, and the core challenge is encoding the boundaries between strings in a way that's unambiguous no matter what's inside them."
You know what I mean, I need a format that is always clear, regardless of content.

# Plan
> "Let me start with the simplest idea first."

The naive approach: join strings with a delimiter like `|`.

```
encode(["hello", "world"]) → "hello|world"
decode("hello|world")      → ["hello", "world"]  ✓
```

Looks fine. But watch what happens when a string contains the delimiter:

```
encode(["he|llo", "world"]) → "he|llo|world"
decode("he|llo|world")      → ["he", "llo", "world"]  ✗  (3 strings, not 2)
```

> "So no matter what character we pick as the delimiter — '#', '|', comma, anything — the same problem exists. If strings can contain any character, no single character is safe."

> "The root issue is that we're using the *content* of the string to mark the *boundary* of the string. That's a contradiction."

### Optimal Approach — length-prefix encoding

> "The fix is to stop relying on content. Instead, we encode the *length* of each string upfront."

Format: for each string, prepend `len(s)` + `"#"` + the string itself.

```
"hello"   → "5#hello"
"world"   → "5#world"
"5#hello" → "7#5#hello"   ← the tricky case still works
""        → "0#"
```

Full example:
```
["hello", "world"] → "5#hello5#world"
```

When decoding, we don't split — we *read with intention*:
1. Scan forward until we hit `#` — that gives us the length
2. Read exactly that many characters — that's the string
3. Move the pointer forward and repeat

> "The `#` here is not separating strings — it's separating the length number from the string content. The length number tells us exactly how many characters to read, so we never care what's inside."

> "Let me verify with the tricky test case: `'7#5#hello'`. We read `7`, then read 7 characters: `'5#hello'`. Correct."

### Excalidraw: What to draw

- **Encoding**: Three boxes (strings) → each gets `len#` prepended → arrow to one long combined string
  - Show the tricky case: `"5#hello"` → `"7#5#hello"`
- **Decoding**: The encoded string as a line of characters, with pointer `i` and `j`
  - `j` scans right until it hits `#`
  - Bracket showing `s[j+1 : j+1+length]` being extracted
  - Arrow showing `i` jumping to the next chunk

### Excalidraw: What to draw

- **Encoding diagram**: Show 3 strings → each gets `len#` prepended → concatenated into one long string
  - `"hi"` → `"2#hi"`, `"5#hello"` (tricky case) → `"7#5#hello"`, `""` → `"0#"`
- **Decoding diagram**: Show pointer `i` scanning the encoded string
  - Find `#` at position `j`, read `s[i:j]` as length, then slice `s[j+1 : j+1+length]`
  - Arrow showing `i` jumping forward to `j+1+length`

### Pseudocode

> "Let me write out the pseudocode first..."

```
encode(strs):
    result = ""
    for each string s in strs:
        result += str(len(s)) + "#" + s
    return result

decode(s):
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        result.append(s[j+1 : j+1+length])
        i = j + 1 + length
    return result
```

### Complexity

> "Time complexity is O(m) for both encode and decode, where m is the total number of characters across all strings. We touch every character exactly once."

> "Space complexity is O(m) because we store the encoded string which is proportional to the total input size."

---

## 3. Implement（4-5 min）

```python
class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
```

### Key implementation notes（話しながら書くポイント）

- `str(len(s)) + "#" + s` — the `#` is a separator between the length number and the string, not between strings
- The inner `while s[j] != "#"` loop finds where the length number ends — this handles multi-digit lengths like `12#`
- `s[j + 1 : j + 1 + length]` — `j+1` skips past the `#`, then we read exactly `length` characters
- `i = j + 1 + length` — we move the pointer `i` to the start of the next encoded chunk
- This handles edge cases automatically: `""` encodes as `"0#"`, and decodes back to `""`

---

## 4. Review & Evaluate（3-4 min）

### Test simulation（trace through by hand）

**Test: `["hi", ""]`**

```
Encode:
  "hi" → "2#hi"
  ""   → "0#"
  encoded = "2#hi0#"

Decode s = "2#hi0#":
  i=0: j moves to 1 (s[1]='#'), length=2, append s[2:4]="hi", i=4
  i=4: j moves to 5 (s[5]='#'), length=0, append s[6:6]="", i=6
  result = ["hi", ""] ✓
```

**Test: `["5#hello"]` — tricky case with '#' in string**

```
Encode:
  "5#hello" → "7#5#hello"

Decode s = "7#5#hello":
  i=0: j moves to 1 (s[1]='#'), length=7, append s[2:9]="5#hello", i=9
  result = ["5#hello"] ✓
```

> "Even though the string contains '5#', our decoder reads exactly 7 characters after the first '#', so it never gets confused."

### Evaluate

> "Time: O(m) — we process every character a constant number of times in both encode and decode."

> "Space: O(m) — the encoded string size is m (characters) plus n (one '#' and length digits per string), which is O(m + n). Since n ≤ m in most cases, we say O(m)."

### Trade-offs & Follow-ups

> "One trade-off here is that we add a small overhead per string — the length prefix. For a million tiny strings, this metadata adds up. But it's still O(m + n), which is optimal."

> "An alternative approach is to use a fixed-width 4-byte header for the length. That way decode doesn't need to scan for '#' — it always reads 4 bytes first. This is how many binary protocols work in practice."

> "If we needed to serialize nested structures — like a list of lists — we could extend this idea by adding another layer of length-prefixed encoding."
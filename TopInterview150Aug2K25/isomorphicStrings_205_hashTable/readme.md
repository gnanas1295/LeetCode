# Isomorphic Strings

## 📝 Problem Statement

You are given two strings, `s` and `t`. Your task is to determine if they are **isomorphic**.

Two strings `s` and `t` are considered isomorphic if the characters in `s` can be replaced to get `t`, according to the following rules:
1.  All occurrences of a character in `s` must be replaced with the same character in `t`.
2.  The order of characters must be preserved.
3.  No two characters from `s` may map to the same character in `t`.
4.  A character may map to itself.

---

## Example

### Example 1:
**Input:** `s = "egg"`, `t = "add"`
**Output:** `true`
**Explanation:** 'e' maps to 'a', and 'g' maps to 'd'. This is a consistent one-to-one mapping.

### Example 2:
**Input:** `s = "foo"`, `t = "bar"`
**Output:** `false`
**Explanation:** The first 'o' would map to 'a', but the second 'o' would need to map to 'r'. This violates the rule that a character must always map to the same character.

### Example 3:
**Input:** `s = "paper"`, `t = "title"`
**Output:** `true`
**Explanation:** 'p' maps to 't', 'a' to 'i', 'e' to 'l', and 'r' to 'e'. This is a valid mapping.

---
## 🧠 Approach: Two-Way Mapping with Hash Maps

The core of this problem is to verify a consistent, **one-to-one mapping** between the characters of `s` and `t`. A simple mapping from `s` to `t` is not enough; we must also ensure the mapping is unique in the other direction.

### Intuition 🗺️
Imagine you are creating a substitution cipher where `s` is the original message and `t` is the coded one. For the cipher to be valid (isomorphic), two conditions must hold true:
1.  **Consistent Encoding:** A letter from the original message must always encode to the same letter in the coded message (e.g., `s = "foo"`, `t = "bar"` fails because `'o'` can't encode to both `'a'` and `'r'`). We can track this with a hash map, `mapS2T`.
2.  **Unambiguous Decoding:** A letter in the coded message must correspond to only one original letter (e.g., `s = "ab"`, `t = "aa"` fails because `'a'` in the coded message can't be decoded to both `'a'` and `'b'`). We can track this with a second, reverse hash map, `mapT2S`.

By maintaining and checking both maps as we iterate through the strings, we can enforce a strict one-to-one relationship.

### Walkthrough
Let's trace `s = "paper"`, `t = "title"`:

| `i` | `s[i]` | `t[i]` | `mapS2T` (State) | `mapT2S` (State) | Action |
|:--- |:--- |:--- |:--- |:--- |:--- |
| 0 | 'p' | 't' | `{}` | `{}` | New mapping. Add `p:t` and `t:p`. |
| 1 | 'a' | 'i' | `{'p':'t'}` | `{'t':'p'}` | New mapping. Add `a:i` and `i:a`. |
| 2 | 'p' | 't' | `{'p':'t', 'a':'i'}` | `{'t':'p', 'i':'a'}` | Existing mapping `p->t` is consistent. |
| 3 | 'e' | 'l' | `{'p':'t', 'a':'i'}` | `{'t':'p', 'i':'a'}` | New mapping. Add `e:l` and `l:e`. |
| 4 | 'r' | 'e' | `{'p':'t', 'a':'i', 'e':'l'}` | `{'t':'p', 'i':'a', 'l':'e'}` | New mapping. Add `r:e` and `e:r`. |

The loop completes successfully, so the strings are isomorphic.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * Where `N` is the length of the strings. We iterate through the strings exactly once.

* **Space Complexity:** $O(k)$
    * Where `k` is the number of unique characters in the strings. Since the problem specifies ASCII characters, the number of unique characters is limited and can be considered constant. Therefore, the space complexity is effectively $O(1)$.

---

## 💻 Code (Python)

This is your solution, which correctly implements the two-map approach. The `print` statements have been removed.

```python
from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS2T = {}
        mapT2S = {}

        for char_s, char_t in zip(s, t):
            # Check for conflicting mappings
            # 1. Does char_s already map to a DIFFERENT char_t?
            # 2. Does char_t already get mapped to by a DIFFERENT char_s?
            if (char_s in mapS2T and mapS2T[char_s] != char_t) or \
               (char_t in mapT2S and mapT2S[char_t] != char_s):
                return False
            
            # If no conflicts, create the mapping
            mapS2T[char_s] = char_t
            mapT2S[char_t] = char_s
            
        return True
```

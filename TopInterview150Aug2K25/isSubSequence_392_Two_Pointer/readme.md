# Is Subsequence

## 📝 Problem Statement

You are given two strings, `s` and `t`. Your task is to determine if `s` is a **subsequence** of `t`.

A **subsequence** is a new string formed from an original string by deleting some (or none) of the characters without changing the relative order of the remaining characters. For example, `"ace"` is a subsequence of `"abcde"`, but `"aec"` is not.

---

## Example

### Example 1:
**Input:** `s = "abc"`, `t = "ahbgdc"`
**Output:** `true`
**Explanation:** The characters 'a', 'b', and 'c' appear in "ahbgdc" in the correct order.

### Example 2:
**Input:** `s = "axc"`, `t = "ahbgdc"`
**Output:** `false`
**Explanation:** The character 'x' does not appear in "ahbgdc", so it's impossible to form the subsequence.

---
## 🧠 Approach: Two Pointers

This problem is a perfect candidate for the **Two-Pointer** technique. We can iterate through both strings at the same time to see if `s` can be formed from `t` while respecting the character order.

### Intuition ➡️
We can use one pointer for our target subsequence `s` (let's call it `s_ptr`) and another for the main string `t` (`t_ptr`).

1.  The `t_ptr` will always move forward, scanning through the available characters in the `t` string.
2.  The `s_ptr` will only move forward when we find the specific character it's currently looking for.

We scan through `t` with `t_ptr`. If `t[t_ptr]` matches `s[s_ptr]`, it means we've found the next character of our subsequence in the correct order, so we advance `s_ptr` to look for the next character. Regardless of a match, `t_ptr` always advances.

If we successfully advance `s_ptr` all the way to the end of string `s`, it means every character in `s` was found in `t` in the correct relative order.



### Walkthrough
Let's trace this logic with `s = "abc"`, `t = "ahbgdc"`:

-   `s_ptr` starts at `0` (pointing to 'a').
-   `t_ptr` starts at `0` (pointing to 'a').

| `t_ptr` | `t[t_ptr]` | `s_ptr` | `s[s_ptr]` | Match? | Action on `s_ptr` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 'a' | 0 | 'a' | **Yes** | `s_ptr` becomes 1 (now looks for 'b') |
| 1 | 'h' | 1 | 'b' | No | - |
| 2 | 'b' | 1 | 'b' | **Yes** | `s_ptr` becomes 2 (now looks for 'c') |
| 3 | 'g' | 2 | 'c' | No | - |
| 4 | 'd' | 2 | 'c' | No | - |
| 5 | 'c' | 2 | 'c' | **Yes** | `s_ptr` becomes 3 |

The loop finishes. We check if `s_ptr` reached the end of `s`. Since `s_ptr` is `3` and `len(s)` is `3`, the condition `s_ptr == len(s)` is true.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * Where `N` is the length of string `t`. In the worst case, we traverse the entire `t` string once.

* **Space Complexity:** $O(1)$
    * We only use a couple of variables for the pointers, so the space required is constant.

---

## 💻 Code (Python)

This is your solution, which correctly implements the optimal two-pointer approach.

```python
from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0  # Pointer for the subsequence s
        t_ptr = 0  # Pointer for the main string t

        # Loop until we have either found all of s or exhausted t
        while s_ptr < len(s) and t_ptr < len(t):
            # If characters match, we've found the next part of the subsequence
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            
            # Always move the pointer for the main string forward
            t_ptr += 1

        # If s_ptr reached the end, it means all characters of s were found
        return s_ptr == len(s)
```

# Find the Index of the First Occurrence in a String

## 📝 Problem Statement

You are given two strings, `needle` and `haystack`. Your task is to find the index of the **first occurrence** of the `needle` string within the `haystack` string.

- If `needle` is a part of `haystack`, return the index where the first match begins.
- If `needle` is not part of `haystack`, return `-1`.

---

## Example

### Example 1:
**Input:** `haystack = "sadbutsad"`, `needle = "sad"`
**Output:** `0`
**Explanation:** "sad" appears at index 0 and index 6. The first occurrence is at index 0.

### Example 2:
**Input:** `haystack = "leetcode"`, `needle = "leeto"`
**Output:** `-1`
**Explanation:** "leeto" does not appear in "leetcode".

---
## ✅ Approach 1: Using Built-in Functions

Most programming languages provide highly optimized, built-in methods for finding substrings. This is almost always the best approach in a real-world scenario due to its simplicity and performance.

### Code (Python)
In Python, the `.find()` string method does exactly what the problem asks for.

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

---
## 🧠 Approach 2: Brute-Force (Sliding Window)

This approach manually implements the search logic without relying on built-in functions. It's a fundamental string-matching technique.

### Intuition 🪟
We can think of this as sliding a "window" with the length of the `needle` across the `haystack`. At each possible starting position in the `haystack`, we check if the substring inside our window is identical to the `needle`.

1.  Start at the first possible position (index 0) in the `haystack`.
2.  Compare the corresponding substring of `haystack` with the `needle`, character by character.
3.  If all characters match, we've found our first occurrence and can return the starting index.
4.  If there's a mismatch, we "slide" our window one position to the right and repeat the check from the next character in the `haystack`.
5.  If we check all possible starting positions and find no match, we return `-1`.



### Code
This is your solution, which correctly implements the brute-force sliding window check.

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # Iterate through all possible starting positions in the haystack
        for i in range(n - m + 1):
            # Check if the substring of haystack matches the needle
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            
            if match:
                return i
        
        return -1
```

### Complexity Analysis
* **Time Complexity:** $O(M \times N)$
    * Where `M` is the length of `haystack` and `N` is the length of `needle`. In the worst case (e.g., `haystack="aaaaaaaaab"`, `needle="aaab"`), we perform `N` comparisons for each of the `M - N + 1` possible starting positions.

* **Space Complexity:** $O(1)$
    * We only use a few variables for pointers, so the space is constant.

### 🚀 A Note on More Advanced Algorithms
For very large strings, the $O(M \times N)$ complexity can be slow. More advanced algorithms like **Knuth-Morris-Pratt (KMP)** can solve this problem in $O(M + N)$ time. KMP works by pre-processing the `needle` to identify repeated patterns, which allows it to "smartly" shift the window by more than one position after a mismatch, avoiding redundant comparisons.

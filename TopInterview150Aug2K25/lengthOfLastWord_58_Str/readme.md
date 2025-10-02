# Length of Last Word

## 📝 Problem Statement

You are given a string `s` which consists of words and spaces. Your task is to return the length of the **last word** in the string.

A **word** is defined as a maximal substring consisting of non-space characters only.

---

## Example

### Example 1:
**Input:** `s = "Hello World"`
**Output:** `5`
**Explanation:** The last word is "World", which has a length of 5.

### Example 2:
**Input:** `s = "   fly me   to   the moon  "`
**Output:** `4`
**Explanation:** The last word is "moon", which has a length of 4.

### Example 3:
**Input:** `s = "luffy is still joyboy"`
**Output:** `6`
**Explanation:** The last word is "joyboy", which has a length of 6.

---
## ✅ Approach 1: Using Built-in Functions

This approach leverages Python's built-in string methods to solve the problem in a highly readable and straightforward manner.

### Intuition
The problem can be broken down into two simple steps:
1.  Isolate all the words from the string.
2.  Find the last word and get its length.

Python's `s.split()` method is perfect for the first step. It automatically handles various spacing issues (like leading/trailing spaces and multiple spaces between words) and returns a clean list of words. From there, we can easily access the last element.

### Code
This is your concise and effective solution.

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() separates the string into a list of words
        words = s.split()
        
        # words[-1] accesses the last element of the list
        return len(words[-1])
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * Where `N` is the length of the string. The `split()` method needs to iterate through the entire string.
* **Space Complexity:** $O(N)$
    * In the worst case (e.g., a string of single-letter words like `"a b c d"`), the list of words created by `split()` could take up space proportional to the original string.

---
## 🚀 Approach 2: Manual Iteration (O(1) Space)

This approach achieves the same result without using built-in splitting functions, which is a common follow-up question in interviews. It is more memory-efficient.

### Intuition
To find the last word, it's most efficient to scan the string from **right to left**.
1.  First, we need to find the actual end of the last word, so we skip any trailing spaces at the end of the string.
2.  Once we find the first non-space character (the last letter of the last word), we can start counting.
3.  We continue counting backwards until we either hit a space or reach the beginning of the string.



### Code
```python
class Solution:
    def lengthOfLastWord_manual(self, s: str) -> int:
        length = 0
        # Start from the end of the string
        i = len(s) - 1

        # 1. Skip all trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # 2. Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * In the worst case, we still traverse the entire string once.
* **Space Complexity:** $O(1)$
    * We only use a couple of variables (`length`, `i`), making this a constant space solution.

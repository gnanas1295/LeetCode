
# 14. Longest Common Prefix

This problem requires finding the longest initial string segment that is common to all strings in a given array.

---

## 📝 Problem Statement

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

---

---

## 🚀 Algorithm: Iterative Prefix Reduction

The provided solution uses a straightforward and effective method where it assumes the first string is the longest common prefix and then shortens it based on the other strings.

1.  **Initialization**: The algorithm starts by assuming the **entire first string** (`strs[0]`) is the longest common prefix.
2.  **Iteration**: It then iterates through the rest of the strings in the array, from the second string to the last.
3.  **Validation and Reduction**: For each string, it checks if that string starts with the current prefix candidate.
    * If it doesn't, the algorithm enters a `while` loop that **repeatedly removes the last character** from the prefix candidate.
    * This reduction process continues until the current string starts with the (now shorter) prefix candidate.
4.  **Edge Case**: If the prefix candidate becomes empty (`""`) at any point during the reduction, it means there is no common prefix, and the function immediately returns `""`.
5.  **Return**: If the outer loop completes, the final state of the prefix candidate is the longest common prefix for all strings, which is then returned.

---

## 📊 Complexity Analysis

Let **n** be the number of strings in the array and **m** be the length of the longest string.

* **Time Complexity**: $O(S)$, where **S** is the sum of all characters in all strings.
    In the worst-case scenario, the algorithm might have to compare every character of every string. For example, if all `n` strings are identical and of length `m`, the total number of character comparisons will be approximately $n \times m$. Thus, the time complexity is proportional to the total number of characters in the input.

* **Space Complexity**: $O(1)$
    The algorithm uses a constant amount of extra space. The space used for the `longestStr` variable does not depend on the number of strings in the input array, only on the length of the first string. This is considered constant auxiliary space.

---

## ⛓️ Constraints

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters if it is non-empty.
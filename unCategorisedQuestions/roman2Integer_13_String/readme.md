# 13. Roman to Integer

This problem involves converting a string of Roman numerals, which represent numbers using a specific set of symbols and rules, into its corresponding integer value.

---

## 📝 Problem Statement

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
| :----: | :---: |
|   I    |   1   |
|   V    |   5   |
|   X    |  10   |
|   L    |  50   |
|   C    |  100  |
|   D    |  500  |
|   M    | 1000  |

Typically, numerals are written from largest to smallest. However, there are six special cases where subtraction is used to represent certain numbers:

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral string, convert it to an integer.

---
---

## 🚀 Algorithm: Right-to-Left Pass

The provided solution cleverly handles both addition and subtraction cases by processing the string from right to left.

1.  **Mapping**: A hash map (dictionary) is created to store the integer value of each Roman numeral symbol.
2.  **Initialization**: The algorithm starts by initializing a total with the value of the **very last symbol** in the string.
3.  **Iteration**: It then iterates backward from the second-to-last symbol to the first.
4.  **Comparison**: In each step, it compares the value of the current symbol (`s[i]`) with the value of the symbol to its right (`s[i+1]`).
    * If the current symbol's value is **less than** the next symbol's value (e.g., 'I' in "IV"), it means this is a subtraction case, so the current symbol's value is **subtracted** from the total.
    * If the current symbol's value is **greater than or equal to** the next symbol's value (e.g., 'V' in "VI"), it's an addition case, and the current symbol's value is **added** to the total.
5.  **Return**: After the loop finishes, the final accumulated total is the correct integer value.

---

## 📊 Complexity Analysis

Let **n** be the length of the input string `s`.

* **Time Complexity**: $O(n)$
    The algorithm involves a single pass through the input string. Since the work done at each character (map lookup, comparison, arithmetic) is constant, the time complexity is linear with respect to the length of the string.

* **Space Complexity**: $O(1)$
    The space required is constant. The hash map stores a fixed number of key-value pairs (7), which does not change based on the input string's length.

---

## ⛓️ Constraints

* `1 <= s.length <= 15`
* `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
* It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.


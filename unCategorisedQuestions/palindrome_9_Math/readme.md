# 9. Palindrome Number

A palindrome is a sequence that reads the same backward as forward. This problem challenges us to determine if a given integer possesses this property.

---

## 📝 Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

---

## 💡 Examples

**Example 1:**

**Input:** `x = 121`
**Output:** `true`
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** `x = -121`
**Output:** `false`
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

**Input:** `x = 10`
**Output:** `false`
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

---

## 🚀 Algorithm: Convert to String

The provided solution uses a simple and intuitive string manipulation approach.

1.  **Convert:** The integer `x` is first converted into its string representation.
2.  **Reverse:** A reversed version of this string is created. In Python, this is easily done with slice notation `[::-1]`.
3.  **Compare:** The original string is compared to the reversed string.
4.  **Return:** If the two strings are identical, the function returns `true`; otherwise, it returns `false`.



---

## 📊 Complexity Analysis

Let **d** be the number of digits in the integer `x`.

* **Time Complexity:** $O(d)$
    The time it takes to convert the integer to a string is proportional to the number of its digits. Reversing and comparing the strings also takes $O(d)$ time. Therefore, the overall time complexity is linear with respect to the number of digits in the input.

* **Space Complexity:** $O(d)$
    Space is required to store the string representation of the number and its reversed copy. This space is directly proportional to the number of digits in the input integer.

---

## ⛓️ Constraints

* The input integer `x` will be within the 32-bit signed integer range: $-2^{31} \le x \le 2^{31} - 1$.

---

## 🤔 Follow Up

This approach is clean and simple, but it requires extra space. Could you solve the problem *without* converting the integer to a string?

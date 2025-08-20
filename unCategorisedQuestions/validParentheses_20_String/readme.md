# 20. Valid Parentheses

This problem is a classic computer science puzzle that uses a stack to validate the structure of a string containing different types of brackets.

---

## 📝 Problem Statement

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

An input string is valid if:
1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

---

## 🚀 Algorithm: Stack-Based Approach

The solution leverages a **stack** data structure, which is perfectly suited for this problem due to its Last-In, First-Out (LIFO) nature. This mirrors how nested brackets must be resolved: the last opening bracket must be the first one to be closed.

1.  **Initialization**: A `stack` is created to keep track of open brackets. A `hash map` is also used to store the valid pairings of closing to opening brackets.
2.  **Iteration**: The algorithm iterates through each character of the input string.
3.  **Character Check**:
    * If the character is an **opening bracket** (`(`, `{`, `[`), it is **pushed** onto the stack.
    * If the character is a **closing bracket** (`)`, `}`, `]`):
        * The algorithm first checks if the stack is empty. If it is, there's no matching open bracket, so the string is invalid.
        * If the stack is not empty, it **pops** the top element.
        * This popped element is then compared with the expected opening bracket from the hash map. If they don't match, the string is invalid.
4.  **Final Validation**: After the loop has processed all characters, the algorithm checks if the stack is empty.
    * If the stack is **empty**, it means every open bracket was correctly matched and closed. The string is **valid**.
    * If the stack is **not empty**, it means there are unclosed opening brackets. The string is **invalid**.

---

## 📊 Complexity Analysis

Let **n** be the length of the input string `s`.

* **Time Complexity**: $O(n)$
    The algorithm involves a single pass through the input string. Each operation within the loop (pushing, popping, and map lookups) takes constant time, $O(1)$. Therefore, the total time complexity is linear with respect to the length of the string.

* **Space Complexity**: $O(n)$
    In the worst-case scenario, the input string may consist entirely of opening brackets (e.g., `"((((["`). In this case, the stack would grow to the size of the input string. Thus, the space complexity is linear with respect to the length of the string.

---

## ⛓️ Constraints

* `1 <= s.length <= 10^4`
* `s` consists of parentheses only `'()[]{}'`.

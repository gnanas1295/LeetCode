# Valid Palindrome

## 📝 Problem Statement

You are given a string `s`. A phrase is considered a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Your task is to return `true` if `s` is a palindrome, or `false` otherwise.

---

## Example

### Example 1:
**Input:** `s = "A man, a plan, a canal: Panama"`
**Output:** `true`
**Explanation:** After sanitizing, the string becomes "amanaplanacanalpanama", which is a palindrome.

### Example 2:
**Input:** `s = "race a car"`
**Output:** `false`
**Explanation:** After sanitizing, the string becomes "raceacar", which is not a palindrome.

### Example 3:
**Input:** `s = " "`
**Output:** `true`
**Explanation:** After removing non-alphanumeric characters, the string becomes empty (`""`). An empty string is a palindrome.

---
## ✅ Approach 1: Sanitize and Reverse

This is a straightforward, two-step approach. First, we clean the input string. Second, we check if the clean string is equal to its reverse.

### Intuition 🧹
The problem has two distinct parts: filtering the string and checking for the palindrome property. We can solve them in order.
1.  **Filter:** Create a new string that contains only the alphanumeric characters from the original string, converted to lowercase.
2.  **Check:** A string is a palindrome if it reads the same forwards and backwards. The simplest way to check this is to compare the string with its reversed version.

### Code
This refines your solution by replacing the complex loop with a simple and direct reversal check.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter and sanitize the string in one line.
        clean_str = "".join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Check if the clean string is equal to its reverse.
        return clean_str == clean_str[::-1]
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the string once to build the new `clean_str`. The reversal and comparison also take $O(N)$ time.
* **Space Complexity:** $O(N)$
    * We use extra space to store the `clean_str`. In the worst case, if all characters are alphanumeric, the new string has the same length as the input.

---
## 🚀 Approach 2: Two Pointers (Optimal Space)

This approach is more memory-efficient as it avoids creating a new string. It works by checking the string from both ends, moving inward.

### Intuition ↔️
We can use two pointers, `left` and `right`, starting at the beginning and end of the original string `s`.
1.  We move the `left` pointer forward and the `right` pointer backward, skipping any characters that are not letters or numbers.
2.  Once both pointers are on alphanumeric characters, we compare them (ignoring case).
3.  If they are not the same, we know it's not a palindrome and can stop immediately.
4.  If they are the same, we move both pointers inward and repeat the process until they meet or cross.



### Code
```python
class Solution:
    def isPalindrome_two_pointers(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it's on an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move right pointer until it's on an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the two characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers inward
            left += 1
            right -= 1
            
        return True
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * In the worst case, each pointer traverses the entire string once.
* **Space Complexity:** $O(1)$
    * We only use a few variables for the pointers, performing the check in-place. This is the most memory-efficient solution.

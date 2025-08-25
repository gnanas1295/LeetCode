# Ransom Note

## 📝 Problem Statement

You are given two strings, `ransomNote` and `magazine`. Your task is to determine if the `ransomNote` can be constructed by using the letters from the `magazine`.

Each letter in the `magazine` can only be used once in your `ransomNote`. Both strings consist of lowercase English letters.

---

## Example

### Example 1:
**Input:** `ransomNote = "a"`, `magazine = "b"`
**Output:** `false`
**Explanation:** The letter 'a' is not available in the magazine.

### Example 2:
**Input:** `ransomNote = "aa"`, `magazine = "ab"`
**Output:** `false`
**Explanation:** The magazine only has one 'a', but the note requires two.

### Example 3:
**Input:** `ransomNote = "aa"`, `magazine = "aab"`
**Output:** `true`
**Explanation:** The magazine has two 'a's and one 'b', which is sufficient to construct the note.

---
## 🧠 Approach: Frequency Counter (Hash Map)

This problem is a classic "counting" problem. We need to check if the `magazine` has enough of each specific character to satisfy the requirements of the `ransomNote`. A **Frequency Counter** (or Hash Map) is the ideal data structure for this.

### Intuition 📖
1.  **Count Supplies:** First, we need an inventory of all the characters available in the `magazine`. We can count the occurrences of each character and store them in a hash map, where the keys are the characters and the values are their frequencies.
2.  **Check Demands:** Once we have our inventory, we can iterate through the `ransomNote` character by character. For each character needed, we check our inventory.
    - If the character is available (its count is greater than 0), we "use it" by decrementing its count in our inventory.
    - If the character is not available (its count is 0), we immediately know it's impossible to form the note, and we can stop and return `false`.
3.  **Conclusion:** If we successfully finish iterating through the entire `ransomNote` without running out of any required characters, it means the note can be constructed.

[Image of Scrabble tiles]

### Walkthrough
Let's trace `ransomNote = "aab"`, `magazine = "baa"`:

1.  **Count characters in `magazine` ("baa"):**
    - The frequency map becomes `{'b': 1, 'a': 2}`.
2

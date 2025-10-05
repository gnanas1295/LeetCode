# Word Pattern

## 📝 Problem Statement

You are given a `pattern` string and a string of words `s`. Your task is to determine if `s` follows the same pattern.

"Follows" means a **full match**, such that there is a **bijection** (a one-to-one and onto mapping) between a letter in the `pattern` and a non-empty word in `s`. This means:
1.  Each letter in `pattern` must map to exactly one word.
2.  Each word in `s` must map to exactly one letter.

---

## Example

### Example 1:
**Input:** `pattern = "abba"`, `s = "dog cat cat dog"`
**Output:** `true`
**Explanation:** 'a' maps to "dog" and 'b' maps to "cat". This is a consistent one-to-one mapping.

### Example 2:
**Input:** `pattern = "abba"`, `s = "dog cat cat fish"`
**Output:** `false`
**Explanation:** The pattern requires the last word to be the same as the first ("dog"), but it is "fish".

### Example 3:
**Input:** `pattern = "aaaa"`, `s = "dog cat cat dog"`
**Output:** `false`
**Explanation:** The pattern requires all words to be the same, but they are not.

---
## 🧠 Approach: Two Hash Maps for Bidirectional Mapping

This problem is a direct extension of the "Isomorphic Strings" concept. The core requirement is to verify a **bijection**, which is a strict one-to-one correspondence between the pattern's characters and the string's words. To ensure this, we must check the mapping in **both directions**.

### Intuition 🗺️
Imagine creating a codebook to translate the `pattern` to `s`. For the translation to be valid:
1.  **Consistent Encoding (`char -> word`):** A character in the pattern must always translate to the same word. For example, if 'a' translates to "dog", it must always be "dog". We can track this with a hash map, `char_to_word`.
2.  **Unambiguous Decoding (`word -> char`):** A word in the result must correspond to only one original character. For example, the word "dog" cannot be the translation for both 'a' and 'b'. We can track this with a second, reverse hash map, `word_to_char`.

By maintaining and checking both maps as we iterate, we can enforce a strict one-to-one relationship.

### Walkthrough
Let's trace `pattern = "abba"`, `s = "dog cat cat dog"`:
1.  First, split `s` into `words = ["dog", "cat", "cat", "dog"]`.
2.  Check lengths: `len(pattern)` is 4, `len(words)` is 4. They match.
3.  Iterate through `(char, word)` pairs:

| `char` | `word` | `char_to_word` (State) | `word_to_char` (State) | Checks | Action |
|:---|:---|:---|:---|:---|:---|
| 'a' | "dog" | `{}` | `{}` | Passes (both new) | Add `a:dog` & `dog:a` |
| 'b' | "cat" | `{'a':'dog'}` | `{'dog':'a'}` | Passes (both new) | Add `b:cat` & `cat:b` |
| 'b' | "cat" | `{'a':'dog','b':'cat'}` | `{'dog':'a','cat':'b'}` | `char_to_word['b'] == "cat"`. Pass. | Continue |
| 'a' | "dog" | `{'a':'dog','b':'cat'}` | `{'dog':'a','cat':'b'}` | `char_to_word['a'] == "dog"`. Pass. | Continue |

The loop completes without any conflicts, so we return `true`.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N + M)$
    * Where `N` is the length of the `pattern` and `M` is the length of the string `s`. The `s.split()` operation takes $O(M)$ and the main loop runs `N` times.

* **Space Complexity:** $O(k + w)$
    * Where `k` is the number of unique characters in the pattern and `w` is the number of unique words in `s`. This space is used to store the mappings in the two hash maps.

---

## 💻 Code (Python)

This is your solution, which correctly implements the optimal two-map approach.

```python
from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        # A bijection is impossible if lengths don't match.
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            # Check the forward mapping (char -> word)
            if char in char_to_word and char_to_word[char] != word:
                return False
            
            # Check the backward mapping (word -> char)
            if word in word_to_char and word_to_char[word] != char:
                return False

            # If no conflicts, establish the mapping
            char_to_word[char] = word
            word_to_char[word] = char

        return True
```

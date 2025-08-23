# H-Index

## 📝 Problem Statement

You are given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`-th paper. Your task is to compute and return the researcher's **h-index**.

According to the [definition on Wikipedia](https://en.wikipedia.org/wiki/H-index), a scientist has an index `h` if `h` of their `N` papers have at least `h` citations each, and the other `N - h` papers have no more than `h` citations each. The goal is to find the **maximum** possible value of `h`.

---

## Example

### Example 1:
**Input:** `citations = [3,0,6,1,5]`
**Output:** `3`
**Explanation:** The researcher has 5 papers with 3, 0, 6, 1, and 5 citations.
- Sorting these gives `[6, 5, 3, 1, 0]`.
- The researcher has **3** papers with at least **3** citations (`6`, `5`, `3`).
- The remaining two papers (`1`, `0`) have no more than 3 citations.
- Therefore, their h-index is 3.

### Example 2:
**Input:** `citations = [1,3,1]`
**Output:** `1`
**Explanation:**
- Sorting gives `[3, 1, 1]`.
- The researcher has **1** paper with at least **1** citation (`3`).
- The h-index cannot be 2, because only one paper has at least 2 citations.
- Therefore, their h-index is 1.

---
## 🧠 Approach and Intuition

The most intuitive way to solve this problem is by **sorting** the array first. The definition of the h-index becomes much easier to check when the citations are in a predictable order.

If we sort the `citations` array in **descending order**, we can iterate through it and ask a simple question at each step:
"Have I seen `k` papers so far, and does the `k`-th paper have at least `k` citations?"

Because the array is sorted from largest to smallest, if the `k`-th paper has at least `k` citations, then all the papers before it are guaranteed to also have at least `k` citations. We just need to find the largest `k` for which this condition is true.



---
### Walkthrough

Let's trace this logic with `citations = [3, 0, 6, 1, 5]`.

1.  **Sort `citations` in descending order:** `[6, 5, 3, 1, 0]`
2.  **Iterate and check the condition:** We use a 1-based count for the number of papers.

| Index `i` | Paper Count (`i+1`) | Citations `citations[i]` | Condition Check: `citations[i] >= (i+1)`? | `h-index` |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 6 | `6 >= 1` is **True** | 1 |
| 1 | 2 | 5 | `5 >= 2` is **True** | 2 |
| 2 | 3 | 3 | `3 >= 3` is **True** | 3 |
| 3 | 4 | 1 | `1 >= 4` is **False** | 3 (Loop breaks) |

The loop stops as soon as the condition is false. The last successful count was **3**, which is our h-index.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N \log N)$
    * The complexity is dominated by the initial sorting of the array. The subsequent loop runs in $O(N)$ time.

* **Space Complexity:** $O(1)$ or $O(\log N)$
    * The space complexity depends on the implementation of the sorting algorithm. Python's `list.sort()` is an in-place sort, which typically uses $O(\log N)$ stack space for recursion in the worst case (or $O(1)$ for some implementations like Timsort).

---

## 💻 Code (Python)

This is your solution, which correctly implements the sorting-based approach. The `print` statement has been removed for a cleaner final version.

```python
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in descending order.
        citations.sort(reverse=True)
        
        h_index = 0
        # Enumerate through the sorted list.
        # 'i' is the 0-based index, so 'i+1' is the number of papers.
        # 'citation_count' is the number of citations for that paper.
        for i, citation_count in enumerate(citations):
            # Check if we have (i+1) papers with at least (i+1) citations.
            if citation_count >= (i + 1):
                h_index = i + 1
            else:
                # Since the list is sorted, we can stop as soon as
                # the condition is not met.
                break
                
        return h_index
```

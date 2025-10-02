# Jump Game II

## 📝 Problem Statement

You are given a 0-indexed integer array `nums` of length `n`. You are initially positioned at **index 0**. Each element `nums[i]` represents the maximum length of a forward jump from index `i`.

Your goal is to reach the last index (`n - 1`) in the **minimum number of jumps**. The test cases are generated such that the last index is always reachable.

---

## (Examples)

### Example 1:
**Input:** `nums = [2,3,1,1,4]`
**Output:** `2`
**Explanation:** The minimum number of jumps is 2.
1. Jump 1 step from index 0 to 1.
2. Jump 3 steps from index 1 to the last index.

### Example 2:
**Input:** `nums = [2,3,0,1,4]`
**Output:** `2`

---
## 🧠 Approach and Intuition

This problem can be solved efficiently using a **Greedy Approach**. The main idea is to think of the jumps in terms of "levels" or "frontiers". For each jump, we want to be as greedy as possible by reaching the farthest possible index.

We use three key variables:
1.  `jumps`: Counts the number of jumps we've made.
2.  `current_reach`: Marks the end of the range we can reach with the current number of `jumps`.
3.  `max_reach`: Tracks the farthest index we can possibly reach from any position within the current level.

The algorithm works like this:
- We start at index 0. The first jump can reach up to `nums[0]`. So, our `current_reach` is `nums[0]`. This is Jump #1.
- We then iterate from our current position through all the indices within our `current_reach`.
- While we are exploring this range, we continuously update `max_reach` to find the best possible "launchpad" for our *next* jump.
- Once our iteration index `i` reaches the `current_reach`, it means we have exhausted all options for the current jump. We must now "commit" to the next jump. We increment our `jumps` counter and update our `current_reach` to the new `max_reach` we found.
- We repeat this until our reach extends to or beyond the last index.



---
### Walkthrough

Let's trace this logic with `nums = [2, 3, 1, 1, 4]`. The loop runs up to the second-to-last element.

| Current Index `i` | `nums[i]` | `max_reach` (Updated) | `current_reach` | Action when `i == current_reach` | `jumps` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 2 | `max(0, 0+2) = 2` | 0 | **JUMP!** Update `current_reach = 2`. | 1 |
| 1 | 3 | `max(2, 1+3) = 4` | 2 | Exploring... | 1 |
| 2 | 1 | `max(4, 2+1) = 4` | 2 | **JUMP!** Update `current_reach = 4`. | 2 |

The loop stops here. At `i = 2`, our new `current_reach` became 4, which is the last index. The number of jumps is **2**. The algorithm correctly found the minimum.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * We iterate through the input array exactly once.

* **Space Complexity:** $O(1)$
    * We only use a few extra variables, which does not depend on the input size.

---

## 💻 Code (Python)

This is your solution, which correctly implements the greedy approach. The variable names have been slightly adjusted for clarity in this explanation.

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Finds the minimum number of jumps to reach the last index.
        """
        jumps = 0
        current_reach = 0
        max_reach = 0

        # We iterate up to the second-to-last element.
        for i in range(len(nums) - 1):
            # Update the farthest we can possibly reach.
            max_reach = max(max_reach, i + nums[i])

            # If we've reached the end of the range for the current jump...
            if i == current_reach:
                # ...we must take another jump.
                jumps += 1
                # The new frontier is the max_reach we found.
                current_reach = max_reach
                
                # An optimization: if the new reach covers the end, we can stop early.
                if current_reach >= len(nums) - 1:
                    break
        
        return jumps
```

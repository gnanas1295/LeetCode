# Jump Game

## 📝 Problem Statement

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element `nums[i]` represents your **maximum jump length** from that position.

The goal is to determine if you can reach the **last index** of the array. Return `true` if you can, and `false` otherwise.

---

##  উদাহরণ (Examples)

### Example 1:
**Input:** `nums = [2,3,1,1,4]`
**Output:** `true`
**Explanation:** You can jump 1 step from index 0 to 1, then 3 steps from index 1 to the last index.

### Example 2:
**Input:** `nums = [3,2,1,0,4]`
**Output:** `false`
**Explanation:** No matter what jumps you make, you will always arrive at index 3. Its maximum jump length is 0, which makes it impossible to proceed to the last index.

---
## 🧠 Approach and Intuition

This problem can be solved with an elegant **Greedy Approach** by working **backwards** from the end of the array.

Instead of asking "Can I reach the end from the start?", we can ask a series of simpler questions: "Which positions can reach the end?"

The intuition is to treat the last index as the initial **goal**. We then iterate from right to left, checking if the current position can reach our `goal`. If it can, then this position becomes our new, closer `goal`. We continue "shifting the goalpost" closer to the start of the array.

If we can successfully move the `goal` all the way to index 0, it means a valid path exists from the start to the end.



---
### Walkthrough

Let's trace this logic with `nums = [2, 3, 1, 1, 4]`. The initial `goal` is the last index, `4`.

| Current Index `i` | `nums[i]` | Jump Range `i + nums[i]` | `goal` (before check) | Can `i` reach `goal`? (`i + nums[i] >= goal`) | `goal` (after check) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3** | 1 | `3 + 1 = 4` | 4 | `4 >= 4` is **True** | **3** |
| **2** | 1 | `2 + 1 = 3` | 3 | `3 >= 3` is **True** | **2** |
| **1** | 3 | `1 + 3 = 4` | 2 | `4 >= 2` is **True** | **1** |
| **0** | 2 | `0 + 2 = 2` | 1 | `2 >= 1` is **True** | **0** |

After the loop, the final `goal` is `0`. Since `goal == 0`, it means the start was able to reach the next "good" stepping stone. We return `true`.

Now let's trace the failing case `nums = [3, 2, 1, 0, 4]`. The initial `goal` is `4`.

| Current Index `i` | `nums[i]` | Jump Range `i + nums[i]` | `goal` (before check) | Can `i` reach `goal`? (`i + nums[i] >= goal`) | `goal` (after check) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3** | 0 | `3 + 0 = 3` | 4 | `3 >= 4` is **False** | 4 |
| **2** | 1 | `2 + 1 = 3` | 4 | `3 >= 4` is **False** | 4 |
| **1** | 2 | `1 + 2 = 3` | 4 | `3 >= 4` is **False** | 4 |
| **0** | 3 | `0 + 3 = 3` | 4 | `3 >= 4` is **False** | 4 |

After the loop, the `goal` is still `4`. Since `goal != 0`, we were never able to find a path back to the start. We return `false`.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * We iterate through the input array exactly once in reverse.

* **Space Complexity:** $O(1)$
    * We only use one extra variable to store the `goal` position, which does not depend on the input size.

---

## 💻 Code (Python)

This is your solution, which correctly implements the backwards greedy approach.

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if the last index can be reached using a greedy approach.
        """
        # The goal is to reach the last index.
        goal = len(nums) - 1

        # Iterate backwards from the second-to-last element.
        for i in range(len(nums) - 2, -1, -1):
            # If the current index can reach or surpass the goal,
            # it becomes the new goal.
            if i + nums[i] >= goal:
                goal = i

        # If we successfully moved the goal to the start, a path exists.
        return goal == 0
```

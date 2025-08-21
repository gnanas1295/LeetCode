# Rotate Array

## 📝 Problem Statement

You are given an integer array `nums`. Your task is to rotate the array to the right by `k` steps, where `k` is a non-negative integer.

The rotation should be done **in-place** with **O(1)** extra space.

---

##  উদাহরণ (Examples)

### Example 1:
**Input:** `nums = [1,2,3,4,5,6,7]`, `k = 3`
**Output:** `[5,6,7,1,2,3,4]`
**Explanation:**
- After 1 step: `[7,1,2,3,4,5,6]`
- After 2 steps: `[6,7,1,2,3,4,5]`
- After 3 steps: `[5,6,7,1,2,3,4]`

### Example 2:
**Input:** `nums = [-1,-100,3,99]`, `k = 2`
**Output:** `[3,99,-1,-100]`
**Explanation:**
- After 1 step: `[99,-1,-100,3]`
- After 2 steps: `[3,99,-1,-100]`

---
## 🧠 Key Insight: Handling `k`

Before approaching the problem, it's important to realize that rotating by `k` steps is the same as rotating by `k % n` steps, where `n` is the length of the array. For example, rotating an array of size 7 by 7 steps results in the original array. Rotating it by 8 steps is the same as rotating it by 1 step. This simple optimization prevents unnecessary rotations.

`k = k % len(nums)`

---
## ✅ Approach 1: Using an Auxiliary Array

This is the most intuitive approach. We can use an extra array to store the rotated version and then copy it back to the original array.

### Intuition
An element at index `i` in the original array will move to a new position at `(i + k) % n`. We can create a temporary copy of the array and use this formula to place each element from the copy into its new, correct position in the original array.

### Code
```python
class Solution:
    def rotate_with_extra_space(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        # Create a copy of the original array
        temp_list = nums.copy()
        
        # Place elements from the copy into their new positions
        for i in range(n):
            nums[(i + k) % n] = temp_list[i]
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the array twice: once to copy it and once to place the elements.
* **Space Complexity:** $O(N)$
    * We use an auxiliary array of the same size as the input.

---
## 🚀 Approach 2: Using Reversals (Optimal In-Place Solution)

This is a clever, non-obvious method that achieves the rotation in-place with $O(1)$ extra space by reversing parts of the array.

### Intuition 🔄
Let's analyze the target array. For `nums = [1,2,3,4,5,6,7]` and `k=3`, the target is `[5,6,7,1,2,3,4]`. The target is formed by taking the last `k` elements and placing them in front of the first `n-k` elements.

The algorithm uses three reversal steps:
1.  **Reverse the entire array.** This places the last `k` elements at the beginning, but they (and the rest of the elements) are in the wrong order.
    `[1,2,3,4,5,6,7]` -> `[7,6,5,4,3,2,1]`
2.  **Reverse the first `k` elements.** This corrects the order of the first part of the array, which is our desired new prefix.
    `[7,6,5]` -> `[5,6,7]`. The array becomes `[5,6,7,4,3,2,1]`.
3.  **Reverse the remaining `n-k` elements.** This corrects the order of the second part of the array, giving us the final result.
    `[4,3,2,1]` -> `[1,2,3,4]`. The array becomes `[5,6,7,1,2,3,4]`.



### Code
This is the solution you implemented.

```python
from typing import List

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """Helper function to reverse a portion of the array."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array in-place using the reversal method.
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return

        # Handle k > n
        k = k % n

        # Step 1: Reverse the entire array
        self.reverse(nums, 0, n - 1)
        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Step 3: Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * Each element in the array is swapped at most twice across all three reversal operations.
* **Space Complexity:** $O(1)$
    * The rotation is performed in-place without using any extra data structures. This satisfies the follow-up.

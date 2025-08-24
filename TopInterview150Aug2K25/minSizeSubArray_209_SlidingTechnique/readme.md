# Minimum Size Subarray Sum

## 📝 Problem Statement

You are given an array of positive integers `nums` and a positive integer `target`.

Your task is to find the **minimal length** of a **contiguous subarray** whose sum is greater than or equal to `target`. If no such subarray exists, you should return `0`.

---

## Example

### Example 1:
**Input:** `target = 7`, `nums = [2,3,1,2,4,3]`
**Output:** `2`
**Explanation:** The subarray `[4,3]` is the shortest one whose sum (7) meets the target.

### Example 2:
**Input:** `target = 4`, `nums = [1,4,4]`
**Output:** `1`
**Explanation:** The subarray `[4]` has a sum of 4, which meets the target with a minimal length of 1.

### Example 3:
**Input:** `target = 11`, `nums = [1,1,1,1,1,1,1,1]`
**Output:** `0`
**Explanation:** The sum of the entire array is 8, so no subarray can sum to 11 or more.

---
## ✅ Approach 1: Sliding Window (O(N) Solution)

This problem is a perfect fit for the **Sliding Window** technique. This approach is highly efficient because it avoids re-calculating sums for overlapping subarrays.

### Intuition 🪟
We can think of a "window" defined by two pointers, `left` and `right`, that slides over the array.
1.  We start with an empty window (`left = 0`, `right = 0`).
2.  We **expand** the window by moving the `right` pointer forward, adding the new element to a running `currentSum`.
3.  Once `currentSum` is greater than or equal to `target`, we have a valid subarray. We record its length.
4.  Now, we try to find a *smaller* valid subarray. We **shrink** the window from the left by moving the `left` pointer forward and subtracting the leftmost element from `currentSum`.
5.  We keep shrinking as long as the `currentSum` remains valid (>= `target`), updating our minimum length each time.
6.  We repeat this process of expanding and shrinking until the `right` pointer has traversed the entire array.



### Code
This is your solution, which correctly implements the Sliding Window pattern.

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 0
        currentSum = 0
        minLen = float('inf')

        # 'right' pointer expands the window
        for right in range(len(nums)):
            currentSum += nums[right]
            
            # When the window sum is valid, try to shrink it
            while currentSum >= target:
                minLen = min(minLen, right - left + 1)
                currentSum -= nums[left]
                left += 1
                
        # If minLen was never updated, no valid subarray was found
        return minLen if minLen != float('inf') else 0
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * Each element is visited at most twice (once by the `right` pointer and once by the `left` pointer).
* **Space Complexity:** $O(1)$
    * We only use a few variables to track the state, so the space is constant.

---
## 🚀 Approach 2: Binary Search with Prefix Sums (O(N log N) Solution)

This approach addresses the follow-up question and uses a different technique.

### Intuition
For any starting index `i`, we are looking for the smallest ending index `j` such that the sum of `nums[i...j]` is at least `target`.

We can pre-calculate the **prefix sums** of the array, where `prefix_sums[k]` is the sum of all elements from `0` to `k-1`. With this, the sum of any subarray `nums[i...j]` can be found in $O(1)$ time by calculating `prefix_sums[j+1] - prefix_sums[i]`.

Our condition becomes: `prefix_sums[j+1] - prefix_sums[i] >= target`.
Rearranging this gives: `prefix_sums[j+1] >= target + prefix_sums[i]`.

Since all numbers in `nums` are positive, the `prefix_sums` array will be strictly increasing (and thus, sorted). This allows us to use **binary search** for each starting index `i` to efficiently find the smallest `j` that satisfies this condition.

### Code
```python
import bisect

class Solution:
    def minSubArrayLen_binary_search(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        # Create the prefix sums array
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + nums[i]
            
        minLen = float('inf')
        
        # For each starting position, find the smallest valid end position
        for i in range(n + 1):
            required_sum = target + prefix_sums[i]
            
            # Use binary search (bisect_left) to find the target
            # It finds an insertion point which comes after (to the right of)
            # any existing entries of required_sum in prefix_sums.
            end_index = bisect.bisect_left(prefix_sums, required_sum)
            
            if end_index != len(prefix_sums):
                minLen = min(minLen, end_index - i)
                
        return minLen if minLen != float('inf') else 0
```

### Complexity Analysis
* **Time Complexity:** $O(N \log N)$
    * We iterate through the array once to build the prefix sums ($O(N)$).
    * We then iterate through the `n` possible start points, and for each one, we perform a binary search ($O(\log N)$).
* **Space Complexity:** $O(N)$
    * We use an extra array to store the prefix sums.

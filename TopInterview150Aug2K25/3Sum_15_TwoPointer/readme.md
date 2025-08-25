# 3Sum

## 📝 Problem Statement

You are given an integer array `nums`. Your task is to find all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that the indices `i`, `j`, and `k` are all different, and the sum of the elements `nums[i] + nums[j] + nums[k]` equals `0`.

The solution set must not contain duplicate triplets. The order of the output and the order within the triplets does not matter.

---

## Example

### Example 1:
**Input:** `nums = [-1,0,1,2,-1,-4]`
**Output:** `[[-1,-1,2],[-1,0,1]]`

### Example 2:
**Input:** `nums = [0,1,1]`
**Output:** `[]`

### Example 3:
**Input:** `nums = [0,0,0]`
**Output:** `[[0,0,0]]`

---
## 🧠 Approach: Sort and Two Pointers

A brute-force solution would involve three nested loops to check every possible triplet, resulting in an $O(N^3)$ time complexity, which is too slow for the given constraints. A much more efficient approach is to first **sort the array** and then use the **Two Pointer** technique.

### Intuition 🎯
1.  **Sort:** By sorting the array, we can easily navigate it and avoid duplicates.
2.  **Iterate and Reduce:** We can iterate through the sorted array with a main pointer `i`. For each element `nums[i]`, we have effectively reduced the problem: we now need to find two other numbers in the rest of the array (from index `i+1` to the end) that sum up to `-nums[i]`.
3.  **Two Pointers:** This "find two numbers that sum to a target" is a classic "Two Sum" problem on a sorted array. We can solve it in linear time using two pointers, `left` and `right`, which start at the beginning and end of the remaining portion of the array. We move these pointers inward based on whether their sum is too small, too large, or exactly equal to our target.



### Handling Duplicates
A key part of this problem is ensuring the output contains only unique triplets. Sorting helps immensely with this. There are two places we need to be careful:
1.  **Skipping the main pointer `i`:** If we have processed `nums[i]`, and the next element `nums[i+1]` is the same, we should skip it. Otherwise, we would generate the exact same set of triplets.
2.  **Skipping pointers after finding a solution:** Once we find a valid triplet `(nums[i], nums[left], nums[right])`, we need to continue our search for other valid pairs. If we simply move `left` by one, but the new `nums[left]` is a duplicate of the old one, we would create a duplicate triplet. Therefore, after finding a solution, we must advance our `left` pointer past all identical elements.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N^2)$
    * The initial sort takes $O(N \log N)$.
    * The main loop runs $N$ times. Inside it, the two-pointer scan takes at most $O(N)$ time. This results in a total of $O(N \log N + N^2)$, which simplifies to $O(N^2)$.

* **Space Complexity:** $O(1)$ or $O(\log N)$
    * The space used for the output list is not counted. The primary extra space comes from the sorting algorithm, which can be $O(\log N)$ or $O(N)$ depending on the implementation. If we consider this, the complexity is not strictly $O(1)$, but it's very efficient.

---

## 💻 Code (Python)

This is your solution, which correctly implements the "Sort and Two-Pointer" strategy with duplicate handling. The `print` statements have been removed.

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to enable the two-pointer approach
        nums.sort()
        results = []

        # Iterate through the array to pick the first element of the triplet
        for i in range(len(nums) - 2):
            # --- Skip duplicate first elements ---
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers for the rest of the array
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # Found a triplet
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # --- Skip duplicate second elements ---
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return results
```

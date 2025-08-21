# Remove Duplicates from Sorted Array II

## 📝 Problem Statement

You are given an integer array `nums` that is sorted in non-decreasing order. Your task is to remove some duplicates **in-place** such that each unique element appears **at most twice**. The relative order of the elements must be preserved.

The final result, consisting of `k` elements, should be placed in the first `k` slots of the `nums` array. The elements beyond `k` do not matter.

Your goal is to return the integer `k`.

**Constraints:**
* You must modify the input array **in-place**.
* You must solve this with **O(1)** extra memory.

---

##  উদাহরণ (Examples)

### Example 1:
**Input:** `nums = [1,1,1,2,2,3]`
**Output:** `5`, `nums = [1,1,2,2,3,_]`
**Explanation:** The function returns `k = 5`. The first five elements of `nums` are modified to `1, 1, 2, 2, 3`.

### Example 2:
**Input:** `nums = [0,0,1,1,1,1,2,3,3]`
**Output:** `7`, `nums = [0,0,1,1,2,3,3,_,_]`
**Explanation:** The function returns `k = 7`. The first seven elements are `0, 0, 1, 1, 2, 3, 3`.

---

## 🧠 Approach and Intuition

The key to solving this problem efficiently is to use a **"Read and Write"** pointer approach. Since the array is sorted, all duplicate elements will be grouped together. We can iterate through the array with a "read" pointer and use a "write" pointer to place elements in their correct final position.

Our solution uses two main variables:
1.  `k`: This acts as the **write pointer**. It keeps track of the next available position in the array where a valid element should be placed. It also represents the length of the valid array so far. We initialize it to `1` because the first element `nums[0]` is always valid.
2.  `l`: This is a simple **counter** to track the occurrences of the current number we are processing. It's `0` if we've seen the number once, and `1` if we've seen it twice.

The algorithm works as follows:
- We iterate through the array from the second element (`i = 1`) to the end.
- At each element `nums[i]`, we compare it to the previous element `nums[i-1]`.
    - **If `nums[i]` is a new number** (i.e., `nums[i] != nums[i-1]`):
        - It's a unique element we haven't seen in this sequence, so we should keep it.
        - We place it at the `k`-th position: `nums[k] = nums[i]`.
        - We increment our write pointer: `k += 1`.
        - We reset our duplicate counter `l` to `0`, as this is the first time we've seen this new number.
    - **If `nums[i]` is a duplicate** (i.e., `nums[i] == nums[i-1]`):
        - We check our duplicate counter `l`. If `l` is `0`, it means this is only the *second* occurrence of this number, which is allowed.
        - We place it at `nums[k]`, increment `k`, and set `l` to `1` to signal that we cannot accept any more duplicates of this number.
        - If `l` is already `1`, we do nothing (`continue`). This effectively skips the third, fourth, etc., occurrences.

Finally, the value of `k` is the length of the modified array, which we return.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * We iterate through the input array `nums` only once.

* **Space Complexity:** $O(1)$
    * We modify the array in-place and use only a few extra variables (`k`, `l`, `i`), which does not depend on the input size.

---

## 💻 Code (Python)

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in-place such that each unique element appears at most twice.
        
        Args:
            nums: A list of integers sorted in non-decreasing order.
        
        Returns:
            The new length of the array after removing excess duplicates.
        """
        # 'k' is the write pointer. The first element is always valid.
        k = 1
        # 'l' counts the occurrences of the current number (0 for one, 1 for two).
        l = 0
        
        # Iterate from the second element to the end of the array.
        for i in range(1, len(nums)):
            # Case 1: The current element is a duplicate of the previous one.
            if nums[i] == nums[i-1]:
                # If we have only seen one occurrence so far (l=0), we can add another.
                if l == 0:
                    nums[k] = nums[i]
                    k += 1
                    l += 1
                # If we have already seen two occurrences (l=1), we skip this element.
                else:
                    continue
            # Case 2: The current element is a new number.
            else:
                nums[k] = nums[i]
                k += 1
                # Reset the occurrence counter for the new number.
                l = 0

        return k
```

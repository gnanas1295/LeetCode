# Product of Array Except Self

## 📝 Problem Statement

You are given an integer array `nums`. Your task is to return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must adhere to the following constraints:
-   The algorithm must run in **$O(n)$ time**.
-   You **cannot** use the division operation.
-   The solution should use **$O(1)$ extra space** (the output array does not count as extra space).

---

## Example

### Example 1:
**Input:** `nums = [1,2,3,4]`
**Output:** `[24,12,8,6]`
**Explanation:**
- `answer[0]` = 2 * 3 * 4 = 24
- `answer[1]` = 1 * 3 * 4 = 12
- `answer[2]` = 1 * 2 * 4 = 8
- `answer[3]` = 1 * 2 * 3 = 6

### Example 2:
**Input:** `nums = [-1,1,0,-3,3]`
**Output:** `[0,0,9,0,0]`

---
## 🧠 Approach: Prefix and Suffix Products

The problem asks for the product of all numbers *except* the one at the current index `i`. This can be broken down into two independent parts:
1.  The product of all numbers to the **left** of index `i`.
2.  The product of all numbers to the **right** of index `i`.

The final answer for `answer[i]` is simply `(product of left elements) * (product of right elements)`.

To solve this efficiently and meet the constraints, we can make **two passes** over the array. We will use the output array itself to store our intermediate calculations, thus achieving $O(1)$ extra space.



### Algorithm Steps
1.  **Initialize:** Create an `answer` array of the same size as `nums`, filling it with `1`s.
2.  **Left Pass (➡️):**
    -   Iterate from left to right. In this pass, we will calculate the product of all elements to the *left* of each index.
    -   We'll use a variable, `prefix_product`, that keeps a running product. For each index `i`, we first set `answer[i]` to the current `prefix_product`, and then we update `prefix_product` by multiplying it with `nums[i]`.
3.  **Right Pass (⬅️):**
    -   Iterate from right to left. Now, `answer[i]` already contains the product of its left-side elements. We just need to multiply it by the product of its right-side elements.
    -   We'll use a `suffix_product` variable. For each index `i`, we first multiply `answer[i]` by the current `suffix_product`, and then we update `suffix_product` by multiplying it with `nums[i]`.

After these two passes, the `answer` array will contain the final correct products.

### Walkthrough
Let's trace `nums = [1, 2, 3, 4]`:
1.  **Initialize:** `answer = [1, 1, 1, 1]`

2.  **Left Pass:**
    -   `prefix = 1`
    -   `i=0`: `answer[0] = 1`. `prefix` becomes `1*1 = 1`. `answer` is `[1, 1, 1, 1]`.
    -   `i=1`: `answer[1] = 1`. `prefix` becomes `1*2 = 2`. `answer` is `[1, 1, 1, 1]`.
    -   `i=2`: `answer[2] = 2`. `prefix` becomes `2*3 = 6`. `answer` is `[1, 1, 2, 1]`.
    -   `i=3`: `answer[3] = 6`. `prefix` becomes `6*4 = 24`. `answer` is `[1, 1, 2, 6]`.
    -   **After left pass:** `answer = [1, 1, 2, 6]` (Each element is the product of numbers to its left).

3.  **Right Pass:**
    -   `suffix = 1`
    -   `i=3`: `answer[3] *= 1` (is 6). `suffix` becomes `1*4 = 4`. `answer` is `[1, 1, 2, 6]`.
    -   `i=2`: `answer[2] *= 4` (is 8). `suffix` becomes `4*3 = 12`. `answer` is `[1, 1, 8, 6]`.
    -   `i=1`: `answer[1] *= 12` (is 12). `suffix` becomes `12*2 = 24`. `answer` is `[1, 12, 8, 6]`.
    -   `i=0`: `answer[0] *= 24` (is 24). `suffix` becomes `24*1 = 24`. `answer` is `[24, 12, 8, 6]`.

4.  **Final Result:** `[24, 12, 8, 6]`

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * We make exactly two passes through the array, which is $O(N) + O(N) = O(N)$.

* **Space Complexity:** $O(1)$
    * As per the follow-up, the output array does not count as extra space. We only use a couple of variables to store the running products, which is constant space.

---

## 💻 Code (Python)

This is your solution, which correctly implements the optimal two-pass approach.

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n

        # First Pass: Calculate prefix products and store them in the answer array.
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        
        # Second Pass: Calculate suffix products and multiply them with the
        # existing prefix products in the answer array.
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        
        return answer
```

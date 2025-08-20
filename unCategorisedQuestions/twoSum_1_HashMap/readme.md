# ⭐ Two Sum Problem

This repository contains an efficient Python solution for the classic "Two Sum" problem.

---

## 📝 Problem Description

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice. You can return the answer in any order.

### Examples

**Example 1:**
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Example 3:**
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

### Constraints

-   `2 <= nums.length <= 10^4`
-   `-10^9 <= nums[i] <= 10^9`
-   `-10^9 <= target <= 10^9`
-   **Only one valid answer exists.**

---

## 💡 Solution Approach

The solution uses a **hash map** (a dictionary in Python) to solve the problem in a single pass, achieving a time complexity better than the brute-force $O(n^2)$ approach.

The core idea is to iterate through the array while keeping track of the numbers we've already seen. For each number `num` in the array, we calculate its **complement** (i.e., `complement = target - num`). This complement is the number we need to find to form the target sum.

Here's the step-by-step logic:
1.  Initialize an empty dictionary called `seenNumbers`. This dictionary will store the numbers we have encountered so far as keys and their corresponding indices as values.
2.  Iterate through the `nums` array using `enumerate` to get both the index (`itr`) and the value (`num`) of each element.
3.  For each `num`, calculate the required `complement` needed to reach the `target`.
4.  Check if this `complement` already exists as a key in the `seenNumbers` dictionary.
    -   If it **exists**, we have found our pair! The value associated with the `complement` key is the index of the first number, and the current `itr` is the index of the second number. We can immediately return `[seenNumbers[complement], itr]`.
    -   If it **does not exist**, it means we haven't found the pair yet. We add the current `num` and its index `itr` to the `seenNumbers` dictionary to make it available for future checks.

This one-pass approach ensures that we find the solution efficiently without needing nested loops.

---

## 🧠 Complexity Analysis

* **Time Complexity: $O(n)$**
    The solution involves a single pass through the `nums` array. For each element, the dictionary lookup and insertion operations take, on average, constant time, $O(1)$. Therefore, the total time complexity is linear with respect to the number of elements in the input array.

* **Space Complexity: $O(n)$**
    In the worst-case scenario, we might need to store all `n` elements from the `nums` array in the `seenNumbers` dictionary before finding the pair (e.g., if the pair is formed by the last two elements). Thus, the space required grows linearly with the size of the input array.

---

## 🚀 How to Use

To run this solution, you can create an instance of the `Solution` class (as defined in the original code) and call the `twoSum` method with your input.

```python
# Assuming the Solution class is defined elsewhere
# solver = Solution()

# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
# print(f"Input: nums={nums1}, target={target1}")
# print(f"Output: {solver.twoSum(nums1, target1)}")  # Expected: [0, 1]

# Example 2
nums2 = [3, 2, 4]
target2 = 6
# print(f"\nInput: nums={nums2}, target={target2}")
# print(f"Output: {solver.twoSum(nums2, target2)}")  # Expected: [1, 2]
```

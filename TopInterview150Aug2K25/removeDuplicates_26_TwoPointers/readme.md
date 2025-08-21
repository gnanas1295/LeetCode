# 26. Remove Duplicates from Sorted Array

This problem is a classic example of the **two-pointer technique** used to modify an array in-place, which is a common requirement for optimizing space complexity.

---

## 📝 Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Your function should:
1.  Modify the array `nums` so that the first `k` elements contain the unique elements in their original order.
2.  Return `k`, the number of unique elements.

The elements beyond the returned `k` do not matter.

---

## 🚀 Algorithm: Two-Pointer Approach

The solution efficiently solves this problem in-place using a two-pointer technique, where one pointer reads the elements and another one writes the unique elements.

1.  **Initialization**:
    * A "write" pointer, `k`, is initialized to `1`. This pointer marks the position for the next unique element to be placed. The first element at index `0` is always considered unique and remains in place.

2.  **Iteration**:
    * A "read" pointer, `i`, iterates through the array starting from the second element (index `1`).

3.  **Comparison and Placement**:
    * In each iteration, the algorithm compares the current element `nums[i]` with the previous element `nums[i-1]`.
    * If `nums[i]` is **different** from `nums[i-1]`, it signifies a new unique element.
    * This unique element `nums[i]` is then copied to the position of the write pointer, `nums[k]`.
    * The write pointer `k` is then incremented to prepare for the next unique element.

4.  **Return Value**:
    * After the loop finishes, the value of `k` represents the total count of unique elements found. This value is returned. The first `k` elements of the array will now be the sorted, unique elements from the original array.

---

## 📊 Complexity Analysis

Let **n** be the number of elements in the input array `nums`.

* **Time Complexity**: $O(n)$
    The algorithm involves a single pass through the array. The read pointer `i` traverses the array from beginning to end once, resulting in a linear time complexity.

* **Space Complexity**: $O(1)$
    The modification is done in-place. The algorithm only uses a few variables to keep track of indices, so the extra space required is constant and does not depend on the size of the input array.

---

## ⛓️ Constraints

* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in **non-decreasing** order.

# 27. Remove Element

This problem focuses on in-place array modification, a common task that tests your understanding of data manipulation without using extra memory. It's another practical application of the two-pointer technique.

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The relative order of the elements that are not equal to `val` may be changed.

Your function should:
1.  Modify the array `nums` such that the first `k` elements contain the elements that are not equal to `val`.
2.  Return `k`, the number of elements that are not equal to `val`.

The elements beyond the returned `k` do not matter, nor does the size of `nums`.

---

---

## 🚀 Algorithm: Two-Pointer Approach

The solution uses a simple and efficient two-pointer technique to achieve the in-place modification. One pointer iterates through the array to find elements to keep, while the other pointer marks where to place them.

1.  **Initialization**: A "write" pointer, `k`, is initialized to `0`. This pointer tracks the next index where an element that is **not** equal to `val` should be placed.
2.  **Iteration**: A "read" pointer, `i`, iterates through the entire array from the first element to the last.
3.  **Condition and Placement**: For each element `nums[i]`, the algorithm checks if it's **not equal** to `val`. If it is, the element is copied to the position of the write pointer (`nums[k] = nums[i]`), and the write pointer `k` is incremented.
4.  **Return Value**: After the loop completes, `k` represents the total count of the elements that were kept. This value is returned.

---

## 📊 Complexity Analysis

Let **n** be the number of elements in the input array `nums`.

* **Time Complexity**: $O(n)$
    The algorithm makes a single pass through the array. Since the read pointer visits each element exactly once, the time complexity is linear.

* **Space Complexity**: $O(1)$
    The array is modified in-place. The only extra space used is for the pointers, which is constant.

---

## ⛓️ Constraints

* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`
* `0 <= val <= 100`

# 88. Merge Sorted Array

This problem is a classic interview question that tests your ability to manipulate arrays in-place. The key challenge is to merge the second array into the first without using extra space, by leveraging the buffer provided at the end of the first array.

---

## 📝 Problem Statement

You are given two integer arrays, `nums1` and `nums2`, sorted in non-decreasing order, and two integers, `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be **stored inside the array `nums1`**. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements are the elements to be merged, and the last `n` elements are set to `0` and should be ignored.

---

## 🚀 Algorithm: Three Pointers (Merge from End)

The most efficient solution avoids overwriting elements in `nums1` by merging the arrays **from the end** towards the beginning. This uses the empty buffer space at the end of `nums1`.

1.  **Initialization**:
    * A pointer `p1` is set to the last valid element of `nums1` (`m - 1`).
    * A pointer `p2` is set to the last element of `nums2` (`n - 1`).
    * A "write" pointer `k` is set to the last index of `nums1` (`m + n - 1`).

2.  **Main Merging Loop**:
    * A `while` loop runs as long as there are elements left to compare in both `nums1` (via `p1`) and `nums2` (via `p2`).
    * Inside the loop, it compares the elements at `nums1[p1]` and `nums2[p2]`.
    * The **larger** of the two elements is placed at the `k`-th position in `nums1`.
    * The pointer corresponding to the larger element is decremented, and the write pointer `k` is always decremented.

3.  **Handle Remaining Elements**:
    * After the main loop, it's possible that `nums2` still has elements left (if `p1` reached the beginning first).
    * A second `while` loop checks if `p2` is still valid and copies any remaining elements from `nums2` into the remaining empty spots at the beginning of `nums1`.
    * If `nums1` has remaining elements, they are already in their correct sorted position, so no further action is needed.

---

## 📊 Complexity Analysis

* **Time Complexity**: $O(m + n)$
    The algorithm makes a single pass through the elements of both arrays. Each element is read and written exactly once.

* **Space Complexity**: $O(1)$
    The merge operation is performed in-place. The only extra space used is for the three pointers, which is constant and does not depend on the input size.

---

## ⛓️ Constraints

* `nums1.length == m + n`
* `nums2.length == n`
* `0 <= m, n <= 200`
* `1 <= m + n <= 200`
* $-10^9 \le$ `nums1[i]`, `nums2[j]` $\le 10^9$

---

## 🤔 Follow Up

The provided solution runs in $O(m + n)$ time, which is optimal for this problem as every element must be considered at least once.

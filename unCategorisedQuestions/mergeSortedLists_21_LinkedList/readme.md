# 21. Merge Two Sorted Lists

This is a fundamental linked list problem that involves combining two sorted lists into a single sorted list by rearranging their nodes.

---

## 📝 Problem Statement

You are given the heads of two sorted linked lists, `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

---

## 🚀 Algorithm: Iterative Merging with a Dummy Node

The solution efficiently merges the two lists using an iterative approach and a **dummy node** to simplify edge cases.

1.  **Initialization**:
    * A `dummy` node is created to act as a placeholder for the start of the new list. This avoids the need for special logic to handle the head of the merged list.
    * A `current` pointer is initialized to the `dummy` node. This pointer will be used to build the new list by attaching the smaller nodes to `current.next`.

2.  **Iterative Merging**:
    * A `while` loop continues as long as both `list1` and `list2` have nodes.
    * Inside the loop, it compares the values of the current nodes from `list1` and `list2`.
    * The node with the **smaller** value is linked to `current.next`.
    * The head pointer of the list from which the node was taken is advanced to its next element.
    * Finally, the `current` pointer is advanced to the newly added node (`current = current.next`).

3.  **Append Remaining Nodes**:
    * After the loop, it's possible one of the lists still has remaining nodes.
    * The algorithm appends the entire remaining portion of whichever list is not empty to the end of the merged list.

4.  **Return Head**:
    * The `dummy` node was a placeholder. The actual merged list begins at `dummy.next`, which is the value returned by the function.

---

## 📊 Complexity Analysis

Let **n** be the number of nodes in `list1` and **m** be the number of nodes in `list2`.

* **Time Complexity**: $O(n + m)$
    The algorithm traverses each node in both lists exactly once. The total number of operations is proportional to the total number of nodes, resulting in a linear time complexity.

* **Space Complexity**: $O(1)$
    The merge is done in-place by rearranging the pointers of the existing nodes. The only extra space used is for a few pointers (`dummy`, `current`), which is constant and does not depend on the size of the input lists.

---

## ⛓️ Constraints

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in **non-decreasing** order.

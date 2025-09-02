# Insert Delete GetRandom O(1)

## 📝 Problem Statement

You are asked to design a data structure that supports the following three operations, all in **average O(1) time complexity**:
1.  `insert(val)`: Inserts an item `val` into the set if not already present.
2.  `remove(val)`: Removes an item `val` from the set if present.
3.  `getRandom()`: Returns a random element from the current set of elements. Each element must have an equal probability of being returned.

---

## Example

```
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

Output:
[null, true, false, true, 2, true, false, 2]
```

---
## ✅ Approach 1: Using a Set (Your Approach)

The most intuitive data structure for this problem is a **hash set** (`set` in Python), as it naturally provides O(1) average time for insertions, deletions, and lookups.

### Intuition
-   **`insert(val)`**: A set automatically handles duplicates. We can check for the value's existence and add it. Both operations are O(1) on average.
-   **`remove(val)`**: Similarly, a set can check for existence and remove an element in O(1) average time.
-   **`getRandom()`**: This is the tricky part. Sets are unordered and don't support indexing.

### Code
This is your solution, which works perfectly for `insert` and `remove`.
```python
import random

class RandomizedSet:
    def __init__(self):
        self.value_set = set()

    def insert(self, val: int) -> bool:
        if val in self.value_set:
            return False
        self.value_set.add(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.value_set:
            self.value_set.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        # This line is O(N), not O(1)
        return random.choice(list(self.value_set))
```

### The Challenge with `getRandom()`
The issue lies in `random.choice(list(self.value_set))`.
-   **`list(self.value_set)`**: This operation converts the entire set into a list. This requires iterating through all `N` elements in the set, making it an **$O(N)$** operation.
-   This violates the problem's constraint that `getRandom` must also be O(1).

---
## 🚀 Approach 2: Hash Map + List (The O(1) Solution)

To achieve O(1) complexity for all operations, we need to combine the strengths of two data structures: a **dynamic array (list)** and a **hash map (dictionary)**.

### Intuition 🗺️
-   A **list** is great for O(1) `getRandom` because we can access any element by its index `list[random_index]`.
-   A **hash map** is great for O(1) `insert` and `remove` because it provides fast lookups. We can use it to store a mapping from a `value` to its `index` in the list.

**The Main Trick: O(1) Removal**
The biggest challenge is removing an element from a list in O(1) time. Removing from the middle requires shifting all subsequent elements, which is O(N). The trick is to avoid this shift:
1.  When you want to remove an element `val` at `index_to_remove`.
2.  Find the **last element** in the list.
3.  **Swap** them: copy the `last_element` to the `index_to_remove`.
4.  Now, simply **pop** the last element off the list. This is an O(1) operation.
5.  Crucially, you must also update the hash map to reflect the new index of the element you moved.



### Walkthrough of `remove(20)`
- **Initial State:** `list = [10, 20, 30, 40]`, `map = {10: 0, 20: 1, 30: 2, 40: 3}`
1.  **Find `20`**: Its index is `1`. The last element is `40`.
2.  **Move Last Element:** Copy `40` to index `1`. `list` is now `[10, 40, 30, 40]`.
3.  **Update Map:** Update the index for `40` in the map. `map` is now `{10: 0, 20: 1, 30: 2, 40: 1}`.
4.  **Pop:** Remove the last element. `list` is now `[10, 40, 30]`.
5.  **Delete:** Delete `20` from the map. Final `map` is `{10: 0, 30: 2, 40: 1}`.

### Code
```python
import random

class RandomizedSet:
    def __init__(self):
        self.val_map = {}  # Maps value to its index in the list
        self.val_list = [] # Stores the actual values

    def insert(self, val: int) -> bool:
        if val in self.val_map:
            return False
        
        self.val_map[val] = len(self.val_list)
        self.val_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_map:
            return False

        # The core "swap and pop" trick
        index_to_remove = self.val_map[val]
        last_element = self.val_list[-1]
        
        # Move the last element to the position of the one being removed
        self.val_list[index_to_remove] = last_element
        self.val_map[last_element] = index_to_remove

        # Pop the last element and remove the target value from the map
        self.val_list.pop()
        del self.val_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.val_list)

```
### Complexity Analysis
* **`insert`**: $O(1)$ on average.
* **`remove`**: $O(1)$ on average.
* **`getRandom`**: $O(1)$.
* **Space Complexity:** $O(N)$ to store the elements.

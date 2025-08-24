# Valid Sudoku

## 📝 Problem Statement

You are given a 9x9 Sudoku board. Your task is to determine if it is **valid**.

The validation only needs to cover the filled cells according to the following three rules:
1.  Each **row** must contain the digits 1-9 without repetition.
2.  Each **column** must contain the digits 1-9 without repetition.
3.  Each of the nine **3x3 sub-boxes** of the grid must contain the digits 1-9 without repetition.

Empty cells are represented by the character `'.'`.

**Note:** A partially filled board that is valid is not necessarily solvable. You only need to check the validity of the filled cells.

---

## Example

Consider the following valid (but incomplete) Sudoku board:
```
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
```
This board would return `true`.

---
## ✅ Approach 1: Separate Checks for Rows, Columns, and Boxes

This approach is straightforward and directly mirrors the problem's rules. We can write separate logic to validate all rows, then all columns, and finally all nine 3x3 boxes.

### Intuition 🔢
The core of this method is to use a **hash set** (`set` in Python) to keep track of the numbers seen in the current row, column, or box. A set provides $O(1)$ average time complexity for insertion and lookup, making it highly efficient for checking duplicates.

The algorithm performs three major steps:
1.  **Validate Rows:** Iterate through each row. For each row, use a new set to check for duplicates. If a duplicate is found, return `false`.
2.  **Validate Columns:** Do the same for each column.
3.  **Validate 3x3 Boxes:** Iterate through each of the nine 3x3 boxes. For each box, use a new set to check for duplicates. The main challenge here is mapping the box's coordinates to the board's coordinates.

### Code
This is your solution, which correctly implements this three-step validation. The `print` statements have been removed for a cleaner final version.

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check Rows
        for r in range(9):
            seen_in_row = set()
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                if num in seen_in_row:
                    return False
                seen_in_row.add(num)

        # 2. Check Columns
        for c in range(9):
            seen_in_col = set()
            for r in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                if num in seen_in_col:
                    return False
                seen_in_col.add(num)

        # 3. Check 3x3 Boxes
        for box_row in range(3):
            for box_col in range(3):
                seen_in_box = set()
                for i in range(3):
                    for j in range(3):
                        r = box_row * 3 + i
                        c = box_col * 3 + j
                        num = board[r][c]
                        if num == '.':
                            continue
                        if num in seen_in_box:
                            return False
                        seen_in_box.add(num)
                        
        return True
```

---
## 🚀 Approach 2: Single Pass

A common optimization is to check all three conditions in a single pass over the board. This avoids iterating over the 81 cells three times.

### Intuition
As we iterate through each cell `board[r][c]`, we can check the validity of its row, column, and box all at once. To do this, we need to maintain sets for *all* 9 rows, 9 columns, and 9 boxes.

- We can use a list of 9 sets for the rows (`rows_seen`).
- We can use another list of 9 sets for the columns (`cols_seen`).
- We can use a third list of 9 sets for the boxes (`boxes_seen`).

The key is to derive the box index from the row and column index. A simple formula for this is: `box_index = (r // 3) * 3 + (c // 3)`.

### Code
```python
class Solution:
    def isValidSudoku_single_pass(self, board: List[List[str]]) -> bool:
        rows_seen = [set() for _ in range(9)]
        cols_seen = [set() for _ in range(9)]
        boxes_seen = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue

                # Check row
                if num in rows_seen[r]:
                    return False
                rows_seen[r].add(num)

                # Check column
                if num in cols_seen[c]:
                    return False
                cols_seen[c].add(num)

                # Check box
                box_index = (r // 3) * 3 + (c // 3)
                if num in boxes_seen[box_index]:
                    return False
                boxes_seen[box_index].add(num)
        
        return True
```

### Complexity Analysis (For both approaches)
* **Time Complexity:** $O(1)$
    * The size of the Sudoku board is fixed at 9x9 (81 cells). The number of operations is constant and does not scale with any input `N`.
* **Space Complexity:** $O(1)$
    * We use hash sets to store seen numbers. The maximum size of any data structure is also constant (e.g., 9 sets, each with a max size of 9).

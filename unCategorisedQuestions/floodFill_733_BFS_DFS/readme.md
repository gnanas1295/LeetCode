# Flood Fill

## 📝 Problem Statement

You are given an `m x n` integer grid `image` representing the pixel values of an image. You are also given a starting pixel coordinate `(sr, sc)` and a new `color`.

Your task is to perform a **flood fill** on the image. This means changing the color of the starting pixel, plus any pixels connected **4-directionally** (up, down, left, right) to the starting pixel that have the same original color, and so on. The process continues until all pixels in the connected region of the original color have been changed to the new `color`.

Return the modified image.

---

## Example

**Input:** `image = [[1,1,1],[1,1,0],[1,0,1]]`, `sr = 1`, `sc = 1`, `color = 2`

**Original Image:**
| 1 | 1 | 1 |
|---|---|---|
| 1 | **1** | 0 |
| 1 | 0 | 1 |

**Output Image:**
| 2 | 2 | 2 |
|---|---|---|
| 2 | **2** | 0 |
| 2 | 0 | 1 |

**Explanation:** The starting pixel at `(1,1)` has the color 1. The algorithm finds all adjacent pixels that are also color 1 and changes them to 2. This process repeats until the entire connected area of '1's has been "filled" with '2's.

---
## 🧠 Approach: Depth-First Search (DFS) via Recursion

This problem is a classic graph traversal task, where each pixel is a node and an "edge" exists between adjacent pixels of the same color. **Depth-First Search (DFS)** is a natural and elegant way to explore this connected region.

### Intuition 🎨
Imagine you have a paintbrush. You start at the given pixel `(sr, sc)` and do the following:
1.  **Check the Color:** See if the pixel's current color is the one you're supposed to change.
2.  **Paint It:** If it is, you paint it with the new `color`. This also serves to "mark" it as visited so you don't paint it again.
3.  **Spread to Neighbors:** You then try to do the same thing for all four of its neighbors (up, down, left, and right).

This process of "paint, then go to a neighbor and repeat" is inherently recursive. We go as "deep" as we can in one direction before backtracking to explore other neighbors.



### Algorithm Steps
1.  Get the `originalColor` of the starting pixel `image[sr][sc]`.
2.  Handle the edge case: if the `originalColor` is already the new `color`, there is nothing to do and we must return immediately to prevent an infinite loop.
3.  Define a recursive helper function, `fill(r, c)`.
4.  Inside `fill(r, c)`:
    a. **Base Cases:** Stop the recursion if the current pixel `(r, c)` is out of bounds OR if its color is not the `originalColor`.
    b. **Action:** If the checks pass, change the color of the current pixel: `image[r][c] = color`.
    c. **Recurse:** Make four recursive calls to `fill` for the neighbors: `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, and `(r, c-1)`.
5.  Start the process by calling `fill(sr, sc)`.
6.  Return the modified `image`.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(M \times N)$
    * Where `M` and `N` are the dimensions of the image. In the worst case, we might have to visit every pixel in the grid once.

* **Space Complexity:** $O(M \times N)$
    * This is due to the recursion stack. In the worst-case scenario (e.g., a spiral or snake-like path that covers the entire grid), the recursion could go as deep as the total number of pixels.

---

## 💻 Code (Python)

This is your solution, which correctly implements the recursive DFS approach.

```python
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        # Edge Case: If the new color is the same as the original, no work is needed.
        if original_color == color:
            return image
        
        def fill(r, c):
            # Base Cases for the recursion:
            # 1. Is the pixel out of bounds?
            # 2. Is the pixel's color NOT the one we're looking for?
            if not (0 <= r < rows and 0 <= c < cols and image[r][c] == original_color):
                return

            # Action: Change the color of the current pixel.
            image[r][c] = color
            
            # Recurse: Call fill for all 4 neighbors.
            fill(r + 1, c)  # Down
            fill(r - 1, c)  # Up
            fill(r, c + 1)  # Right
            fill(r, c - 1)  # Left
        
        # Start the recursive process from the initial pixel.
        fill(sr, sc)

        return image
```

# Gas Station

## 📝 Problem Statement

You are given a circular route with `n` gas stations. At station `i`, you can get `gas[i]` fuel. To travel from station `i` to `i+1`, it costs `cost[i]` fuel. You start with an empty tank at one of the stations.

Your task is to find the starting gas station's index that allows you to travel around the entire circuit once in a clockwise direction.
- If a solution exists, it is **guaranteed to be unique**.
- If you cannot complete the circuit, return `-1`.

---

## Example

### Example 1:
**Input:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`
**Output:** `3`
**Explanation:** Starting at index 3 (where `gas=4`), you can successfully travel through stations 4, 0, 1, 2, and back to 3.

### Example 2:
**Input:** `gas = [2,3,4]`, `cost = [3,4,3]`
**Output:** `-1`
**Explanation:** No matter where you start, you will run out of gas before completing the circuit.

---
## 🧠 Approach: One-Pass Greedy Solution

This problem, which seems like it might require checking every possible starting point, can be solved in a single pass using a greedy approach with two key insights.

### Intuition ⛽
1.  **Can a circuit be completed at all?**
    A full circuit is only possible if the total amount of gas available is greater than or equal to the total cost of travel. If `sum(gas) < sum(cost)`, it's impossible to finish, no matter where you start. This is a quick check we can do first.

2.  **How do we find the unique starting point?**
    If we know a solution exists (from the check above), we can find it by iterating through the stations. We'll keep track of our current fuel tank level. Let's assume we start at index 0.
    - As we travel from station `i` to `i+1`, we update our tank: `tank += gas[i] - cost[i]`.
    - If at any point our `tank` drops below zero, it means we can't reach station `i+1` from our assumed start.
    - **The Greedy Insight:** If you can't get from station `A` to `C` because you ran out of fuel at station `B`, then you *definitely* can't make it starting from any station between `A` and `B` either. You would have started with even less fuel. Therefore, if we get stuck at station `i`, the next possible starting point **must** be `i+1`. We can then reset our tank and continue the check from this new potential starting point.

Because we already confirmed that a solution exists, the starting point we have at the end of our single pass must be the correct one.



### Walkthrough
Let's trace `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`.
-   `sum(gas)` = 15, `sum(cost)` = 15. Since `15 >= 15`, a solution exists.
-   Let's create a `diff` array for `gas[i] - cost[i]` for simplicity: `[-2, -2, -2, 3, 3]`

| Current Index `i` | `diff[i]` | `tank` (before) | `tank` (after adding `diff[i]`) | Action if `tank < 0` | `start_index` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | -2 | 0 | -2 | `tank < 0`. Reset `tank=0`. Set `start_index=1`. | 1 |
| 1 | -2 | 0 | -2 | `tank < 0`. Reset `tank=0`. Set `start_index=2`. | 2 |
| 2 | -2 | 0 | -2 | `tank < 0`. Reset `tank=0`. Set `start_index=3`. | 3 |
| 3 | 3 | 0 | 3 | `tank >= 0`. Continue. | 3 |
| 4 | 3 | 3 | 6 | `tank >= 0`. Continue. | 3 |

The loop finishes. The final `start_index` is **3**.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * The initial sum check takes $O(N)$. The main loop iterates through the array once. The total time is $O(N) + O(N) = O(N)$.

* **Space Complexity:** $O(1)$
    * We only use a few variables to keep track of the state, regardless of the input size.

---

## 💻 Code (Python)

This is a slightly refactored version of your solution that uses a single `tank` variable to track the fuel balance, aligning with the explanation.

```python
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1. Check if a solution is possible at all.
        if sum(gas) < sum(cost):
            return -1
        
        # 2. Find the unique starting point.
        start_index = 0
        tank = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            
            # If we run out of gas, this can't be the start.
            # The next station is the new candidate start point.
            if tank < 0:
                start_index = i + 1
                tank = 0
                
        return start_index
```

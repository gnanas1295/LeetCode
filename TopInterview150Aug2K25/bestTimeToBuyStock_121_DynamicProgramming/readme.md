# Best Time to Buy and Sell Stock

## 📝 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

The goal is to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this single transaction. If you cannot achieve any profit (i.e., the price only goes down), you should return `0`.

---

##  উদাহরণ (Examples)

### Example 1:
**Input:** `prices = [7,1,5,3,6,4]`
**Output:** `5`
**Explanation:** The best transaction is to buy on day 2 (price = 1) and sell on day 5 (price = 6). The profit is `6 - 1 = 5`. Note that you cannot buy on day 2 and sell on day 1, as you must buy before you sell.

### Example 2:
**Input:** `prices = [7,6,4,3,1]`
**Output:** `0`
**Explanation:** In this scenario, the stock price is always decreasing. No transaction can yield a profit, so the maximum profit is 0.

---
## 🧠 Approach and Intuition

The problem can be solved efficiently in a **single pass**. The core idea is to iterate through the stock prices while keeping track of two key pieces of information:
1.  The lowest stock price encountered so far (`lowestPrice`).
2.  The maximum profit seen so far (`maxProfit`).

Think of it like walking along a timeline of stock prices. At any given day, you can choose to "sell". The profit you would make is the current day's price minus the lowest price you could have possibly bought it for in the past. Our goal is to find the day where this difference is the largest.



The algorithm works as follows:
- We initialize `lowestPrice` to infinity (`float('inf')`) so that the price on the very first day is guaranteed to be lower.
- We initialize `maxProfit` to `0`, as profit cannot be negative.
- We then loop through each `price` in the `prices` array.
    - First, we calculate the `potentialProfit` we could get by selling at the current `price`, based on the `lowestPrice` seen *before* today.
    - We update our `maxProfit` if this `potentialProfit` is greater than the current `maxProfit`.
    - **After** checking for profit, we update our `lowestPrice` by comparing it with the current day's `price`. This ensures that for any given day, `lowestPrice` always represents a day in the past.

---
### Walkthrough

Let's trace the algorithm with `prices = [7, 1, 5, 3, 6, 4]`:

| Current `price` | `lowestPrice` (before check) | `potentialProfit` (`price` - `lowestPrice`) | `maxProfit` (after check) | `lowestPrice` (after update) |
| :--- | :--- | :--- | :--- | :--- |
| **7** | `inf` | `-inf` | 0 | 7 |
| **1** | 7 | `1 - 7 = -6` | 0 | 1 |
| **5** | 1 | `5 - 1 = 4` | 4 | 1 |
| **3** | 1 | `3 - 1 = 2` | 4 | 1 |
| **6** | 1 | `6 - 1 = 5` | 5 | 1 |
| **4** | 1 | `4 - 1 = 3` | 5 | 1 |

The final `maxProfit` is **5**.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * We iterate through the input array `prices` exactly once.

* **Space Complexity:** $O(1)$
    * We only use two extra variables (`lowestPrice` and `profit`) which does not depend on the input size.

---

## 💻 Code (Python)

This is the cleaned-up version of the solution you provided.

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from a single buy-and-sell transaction.
        """
        if not prices:
            return 0
        
        lowestPrice = float('inf')
        maxProfit = 0
        
        for price in prices:
            # Calculate potential profit if we sell today
            potentialProfit = price - lowestPrice
            
            # Update maxProfit if this is the best so far
            maxProfit = max(maxProfit, potentialProfit)
            
            # Update the lowest price seen so far
            lowestPrice = min(price, lowestPrice)
            
        return maxProfit

```

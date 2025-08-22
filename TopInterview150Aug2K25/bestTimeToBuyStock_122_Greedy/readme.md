# Best Time to Buy and Sell Stock II

## 📝 Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Your goal is to find and return the **maximum profit** you can achieve by making any number of transactions.

---

##  উদাহরণ (Examples)

### Example 1:
**Input:** `prices = [7,1,5,3,6,4]`
**Output:** `7`
**Explanation:**
- Buy on day 2 (price = 1) and sell on day 3 (price = 5), for a profit of `5 - 1 = 4`.
- Then, buy on day 4 (price = 3) and sell on day 5 (price = 6), for a profit of `6 - 3 = 3`.
- The total profit is `4 + 3 = 7`.

### Example 2:
**Input:** `prices = [1,2,3,4,5]`
**Output:** `4`
**Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), for a profit of `5 - 1 = 4`. Note that this is equivalent to buying and selling on each consecutive day.

---
## 🧠 Approach and Intuition

This problem seems more complex than buying and selling just once, but the solution is surprisingly simpler. The key insight is that we don't need to find the next lowest "valley" and highest "peak". Since we can complete as many transactions as we want, we can simply capture every single opportunity for profit.

The total profit is the sum of all positive price changes from one day to the next.



Consider a continuous price increase from `1` to `5`: `[1, 2, 3, 4, 5]`. The maximum profit is `5 - 1 = 4`. Notice that this is the same as the sum of the daily profits:
`(2 - 1) + (3 - 2) + (4 - 3) + (5 - 4) = 1 + 1 + 1 + 1 = 4`

This means we can use a **greedy approach**: if the price goes up from yesterday to today, we "buy" yesterday and "sell" today, adding that small profit to our total. If the price goes down, we simply do nothing.

This strategy works because it accumulates all the upward movements in the stock price, which is the definition of profit.

---
### Walkthrough

Let's trace this simple logic with `prices = [7, 1, 5, 3, 6, 4]`:

| Current Day `i` | `prices[i]` | Previous Day `prices[i-1]` | Daily Change `(prices[i] - prices[i-1])` | Action | `totalProfit` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 7 | -6 | Price dropped. Do nothing. | 0 |
| 2 | 5 | 1 | +4 | Price rose. Add profit. | 4 |
| 3 | 3 | 5 | -2 | Price dropped. Do nothing. | 4 |
| 4 | 6 | 3 | +3 | Price rose. Add profit. | 7 |
| 5 | 4 | 6 | -2 | Price dropped. Do nothing. | 7 |

The final `totalProfit` is **7**.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$
    * We iterate through the input array `prices` exactly once.

* **Space Complexity:** $O(1)$
    * We only use one extra variable (`maxProfit`) which does not depend on the input size.

---

## 💻 Code (Python)

This is a clean implementation of the greedy approach.

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from multiple buy-and-sell transactions.
        """
        # It's impossible to have a transaction with less than 2 days.
        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        
        # Iterate from the second day to the end
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, we make a profit
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
                
        return maxProfit

```

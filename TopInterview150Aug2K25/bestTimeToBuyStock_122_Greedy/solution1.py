# from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0

#         finalProfit = 0
#         profit = 0
#         lowestValue = float("inf")
#         highestValue = 0
#         for i in range(len(prices)):
#             potentialProfit = prices[i] - lowestValue

#             lowestValue = min(lowestValue, prices[i])

#             profit = max(potentialProfit, profit)

#             if (prices[i] < prices[i - 1]) and profit:
#                 print("Coming Here")
#                 lowestValue = prices[i]
#                 finalProfit += profit
#                 profit = 0

#         if profit:
#             finalProfit += profit
#         return finalProfit

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

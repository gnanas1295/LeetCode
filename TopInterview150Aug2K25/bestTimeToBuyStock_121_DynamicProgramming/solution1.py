# from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         profits = 0
#         for i in range(len(prices) - 1, -1, -1):
#             j = 0
#             while j < i:
#                 if (prices[i] - prices[j]) > profits:
#                     profits = prices[i] - prices[j]
#                 j += 1

#         return profits

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lowestPrice = float("inf")
        profit = 0
        for price in prices:
            potentialProfit = price - lowestPrice

            profit = max(profit, potentialProfit)

            lowestPrice = min(price, lowestPrice)
        return profit

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        startingPoint = 0
        totalGas = 0
        totalCost = 0

        for x in range(len(gas)):
            totalGas += gas[x]
            totalCost += cost[x]
            if totalGas < totalCost:
                startingPoint = x + 1
                totalGas = 0
                totalCost = 0

        return startingPoint

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        valueToBeReached = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= valueToBeReached:
                valueToBeReached = i

        return valueToBeReached == 0

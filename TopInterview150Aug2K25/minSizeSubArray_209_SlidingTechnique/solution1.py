from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        minLen = float("inf")
        currentSum = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                minLen = min(minLen, right - left + 1)
                currentSum -= nums[left]
                left += 1
        if minLen == float("inf"):
            return 0
        else:
            return minLen

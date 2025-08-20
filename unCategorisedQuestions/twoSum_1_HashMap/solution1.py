class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumbers = {}

        for itr, num in enumerate(nums):
            complement = target - num

            if complement in seenNumbers:
                return [seenNumbers[complement], itr]

            seenNumbers[num] = itr

# from itertools import combinations
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         combi = combinations(nums, 3)
#         # print(*combi)
#         combiUniqueWithZero = [i for i in combi if sum(i) == 0]
#         # for i in combi:
#         #     print(sum(i))
#         print(sorted(combiUniqueWithZero))
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        uniqueSets = []
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            currentSum = 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    uniqueSets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return uniqueSets

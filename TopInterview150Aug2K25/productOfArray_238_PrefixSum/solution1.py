from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lenOfNums = len(nums)
        finalList = [1] * lenOfNums

        prefixProduct = 1
        for x in range(lenOfNums):
            finalList[x] = prefixProduct
            prefixProduct *= nums[x]

        suffixProduct = 1
        for x in range(lenOfNums - 1, -1, -1):
            finalList[x] *= suffixProduct
            suffixProduct *= nums[x]

        return finalList

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        l = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if l == 0:
                    print("Here 1")
                    nums[k] = nums[i]
                    k += 1
                    l += 1
                else:
                    print("Here 2")
                    continue
            else:
                print("Here 3")
                nums[k] = nums[i]
                k += 1
                l = 0

        return k

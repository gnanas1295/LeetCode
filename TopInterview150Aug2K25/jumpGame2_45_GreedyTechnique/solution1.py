from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        maxValueToReach = len(nums) - 1
        currentPosition = 0
        maxValueFromCurrentPosition = 0
        noOfJumps = 0

        for i in range(len(nums) - 1):
            maxValueFromCurrentPosition = max(maxValueFromCurrentPosition, i + nums[i])

            if currentPosition == i:
                noOfJumps += 1

                currentPosition = maxValueFromCurrentPosition

                if currentPosition >= maxValueToReach:
                    break

        return noOfJumps

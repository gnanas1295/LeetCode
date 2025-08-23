# from typing import List


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         finalStr = "".join(char.lower() for char in s if char.isalnum())
#         print(finalStr)
#         if not finalStr:
#             return True

#         for i in range(len(finalStr)):
#             if i == len(finalStr) - 1 - i:
#                 print(i)
#                 print(len(finalStr) - i - 1)
#                 return True
#             if len(finalStr) - 1 - i == 0:
#                 return True
#             if finalStr[i] == finalStr[len(finalStr) - 1 - i]:
#                 continue
#             else:
#                 return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalStr = "".join(char.lower() for char in s if char.isalnum())
        print(finalStr)

        return finalStr == finalStr[::-1]

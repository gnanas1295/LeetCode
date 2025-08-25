from typing import List


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # print(ord('a'))

#         if len(magazine) < len(ransomNote):
#             return False

#         magazine = sorted(magazine)

#         for char in sorted(ransomNote):
#             if char in magazine:
#                 magazine.remove(char)
#             else:
#                 return False
#         return True

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        magazineCount = Counter(magazine)
        print(magazineCount)

        for char in ransomNote:
            if magazineCount[char]:
                magazineCount[char] -= 1
            else:
                return False
        return True

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:

#         sCheckIndex = 0

#         if not s:
#             return True

#         for i in t:
#             if i == s[sCheckIndex]:
#                 if sCheckIndex == (len(s) - 1):
#                     return True
#                 sCheckIndex += 1
#                 continue
#         return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        tPointer = 0

        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            tPointer += 1

        return sPointer == len(s)


# import collections
# import bisect
# from typing import List


# class Solution:
#     # def __init__(self, t: str):
#     #     self.charIndicies = collections.defaultdict(list)
#     #     for char, index in enumerate(t):
#     #         self.charIndicies[char].append(index)

#     def isSubsequence(self, s: str, t: str) -> bool:
#         self.charIndicies = collections.defaultdict(list)
#         for index, char in enumerate(t):
#             self.charIndicies[char].append(index)

#         currentTIndex = -1

#         for charS in s:
#             indicesList = self.charIndicies[charS]

#             if not indicesList:
#                 return False

#             insertionPoint = bisect.bisect_right(indicesList, currentTIndex)

#             if insertionPoint == len(indicesList):
#                 return False

#             currentTIndex = indicesList[insertionPoint]

#         return True

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # return haystack.find(needle)
        for i in range(0, len(haystack) - len(needle) + 1, 1):
            if haystack[i : i + len(needle)] == needle:
                return i
            # for j in range(len(needle)):
            #     if haystack[i + j] != needle[j]:
            #         break
            #     if j == len(needle) - 1:
            #         return i

        return -1

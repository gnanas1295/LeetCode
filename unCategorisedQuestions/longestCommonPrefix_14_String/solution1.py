class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestStr = strs[0]

        for str in range(1, len(strs)):

            while not strs[str].startswith(longestStr):
                longestStr = longestStr[:-1]
                if not longestStr:
                    return ""
        return longestStr

# from collections import Counter


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if sorted(Counter(s).values()) == sorted(Counter(t).values()):
#             return True
#         return False


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS2T = {}
        mapT2S = {}

        for i in range(len(s)):
            if s[i] in mapS2T:
                if mapS2T[s[i]] == t[i]:
                    continue
                else:
                    return False
            elif t[i] in mapT2S:
                if mapT2S[t[i]] == s[i]:
                    continue
                else:
                    return False
            mapS2T[s[i]] = t[i]
            mapT2S[t[i]] = s[i]

        print(mapS2T)
        print(mapT2S)
        return True

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         tempList = list(s.split(" "))
#         charMatch = {}

#         if len(tempList) != len(pattern):
#             return False

#         for i in range(len(tempList)):
#             if tempList[i] in charMatch:
#                 if charMatch[tempList[i]] != pattern[i]:
#                     return False
#                 continue
#             elif pattern[i] in charMatch.values():
#                 return False
#             charMatch[tempList[i]] = pattern[i]


#         return True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False

            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True

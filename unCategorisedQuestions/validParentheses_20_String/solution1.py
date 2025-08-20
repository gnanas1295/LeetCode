import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mappings:

                topElement = stack.pop() if stack else "#"

                if mappings[char] != topElement:
                    return False
            else:
                stack.append(char)

        return not stack

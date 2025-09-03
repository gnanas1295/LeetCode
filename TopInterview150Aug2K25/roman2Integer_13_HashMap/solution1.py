class Solution:
    def romanToInt(self, s: str) -> int:
        romanMapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        finalValue = romanMapping[s[-1]]

        for itr in range(len(s) - 2, -1, -1):
            if romanMapping[s[itr]] < romanMapping[s[itr + 1]]:
                finalValue -= romanMapping[s[itr]]
            else:
                finalValue += romanMapping[s[itr]]

        return finalValue

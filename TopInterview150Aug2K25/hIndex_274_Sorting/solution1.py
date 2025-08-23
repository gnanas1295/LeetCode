from typing import List
from collections import Counter


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count = 0
        for key, value in enumerate(citations):
            print(key, value)
            if value >= (key + 1):
                count += 1
            else:
                break
        return count

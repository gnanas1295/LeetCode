from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = Counter(nums).most_common()
        return counters[0][0]

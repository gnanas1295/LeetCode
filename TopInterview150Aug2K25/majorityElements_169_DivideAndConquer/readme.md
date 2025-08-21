# Majority Element

## 📝 Problem Statement

Given an array `nums` of size `n`, your task is to find and return the **majority element**.

The majority element is defined as the element that appears **more than** `⌊n / 2⌋` times. A key assumption is that the majority element is guaranteed to exist in the array.

---

##   উদাহরণ (Examples)

### Example 1:
**Input:** `nums = [3,2,3]`
**Output:** `3`
**Explanation:** `3` appears 2 times, which is more than `⌊3 / 2⌋ = 1`.

### Example 2:
**Input:** `nums = [2,2,1,1,1,2,2]`
**Output:** `2`
**Explanation:** `2` appears 4 times, which is more than `⌊7 / 2⌋ = 3`.

---

## ✅ Approach 1: Using a Hash Map (Counter)

This is a straightforward and intuitive approach. The idea is to count the occurrences of every element in the array and then identify which element appears most frequently.

### Intuition
If we know the count of every number, we can easily find the majority element. A hash map (or a dictionary in Python) is the perfect data structure for this task, as it allows us to store key-value pairs of `(element, frequency)`. Python's `collections.Counter` is a specialized dictionary that makes this process even simpler.

### Code (Your Solution)
This solution is clean, readable, and correctly solves the problem.

```python
from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element using a frequency counter.
        """
        # Count frequencies of all elements
        counters = Counter(nums)
        # .most_common(1) returns a list like [ (element, count) ]
        return counters.most_common(1)[0][0]

```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * Building the `Counter` requires iterating through all `N` elements once.
* **Space Complexity:** $O(k)$
    * Where `k` is the number of unique elements in the array. In the worst-case scenario, `k` could be close to `N`, so the space complexity is effectively $O(N)$. This does **not** satisfy the follow-up requirement for $O(1)$ space.

---

## 🚀 Approach 2: Boyer-Moore Voting Algorithm (Optimal Solution)

This clever algorithm solves the problem in linear time and constant space, directly addressing the follow-up question.

### Intuition 🗳️
Imagine the array is a sequence of votes for different candidates. The majority element is the candidate who has more votes than all other candidates combined.

The Boyer-Moore algorithm works by "canceling out" votes.
1.  We start with a `candidate` and a `count`.
2.  We iterate through the array. If we see an element that matches our `candidate`, we increment `count`. If we see a different element, we decrement `count`.
3.  If `count` ever reaches `0`, it means the current `candidate` has been "canceled out" by an equal number of opponents. We discard our old candidate and pick the current element as the new `candidate`.

Because the majority element appears more than `n/2` times, it is guaranteed to survive this cancellation process and be the final `candidate` remaining.



### Algorithm Steps
1.  Initialize `candidate = None` and `count = 0`.
2.  Loop through each `num` in `nums`.
3.  If `count` is `0`, set `candidate = num`.
4.  If `num` is the same as `candidate`, increment `count`. Otherwise, decrement `count`.
5.  After the loop, `candidate` will hold the majority element.

### Code
```python
from typing import List

class Solution:
    def majorityElement_optimal(self, nums: List[int]) -> int:
        """
        Finds the majority element using the Boyer-Moore Voting Algorithm.
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
```

### Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the input array only once.
* **Space Complexity:** $O(1)$
    * We only use two extra variables (`candidate` and `count`), regardless of the input size. This successfully meets the follow-up constraint.

import unittest
from solution1 import Solution

class TestMergeSortedArray(unittest.TestCase):

    def test_merge(self):
        sol = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

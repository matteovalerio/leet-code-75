"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

from typing import List
from format_utils import format_solution


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1.difference(set2)), list(set2.difference(set1))]


if __name__ == "__main__":
    sol = Solution()
    input1 = [1, 2, 3]
    input2 = [2, 4, 6]
    expected = [[1, 3], [4, 6]]
    print(
        format_solution([input1, input2], expected, sol.findDifference(input1, input2))
    )

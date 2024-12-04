"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

from typing import List
from format_utils import format_solution


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = [0] * len(nums)
        sumLeft[0] = nums[0]
        for x in range(1, len(nums)):
            sumLeft[x] = sumLeft[x - 1] + nums[x]
        sumRight = 0
        index = -1
        for x in range(len(nums) - 1, -1, -1):
            sumRight += nums[x]
            if sumLeft[x] == sumRight:
                index = x
        return index


if __name__ == "__main__":
    sol = Solution()

    input = [1, 7, 3, 6, 5, 6]
    expected = 3
    print(format_solution(input, expected, sol.pivotIndex(input)))

    input = [1, 2, 3]
    expected = -1
    print(format_solution(input, expected, sol.pivotIndex(input)))

    input = [2, -1, 1]
    expected = 0
    print(format_solution(input, expected, sol.pivotIndex(input)))

    input = [-1, -1, 0, 0, -1, -1]
    expected = 2
    print(format_solution(input, expected, sol.pivotIndex(input)))

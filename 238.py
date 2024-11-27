# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


import copy
from typing import List

from format_utils import format_solution


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # requirement O(n) -> so i must iterate the list one time
        # [1,2,3,4]
        results = [1] * len(nums)
        # left
        for x in range(1, len(nums)):
            results[x] = nums[x - 1] * results[x - 1]
        # [1, 1, 2, 6]
        print(results)
        # right
        rightMult = 1
        for x in range(len(nums) - 2, -1, -1):
            print(
                f"x: {x} - results[x]: {results[x]} - nums[x+1]: {nums[x + 1]} - results: {results}"
            )
            rightMult *= nums[x + 1]
            results[x] *= rightMult

        #
        return results


def main():
    sol = Solution()
    print(
        format_solution(
            [1, 2, 3, 4], [24, 12.8, 6], sol.productExceptSelf([1, 2, 3, 4])
        )
    )
    print(
        format_solution(
            [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], sol.productExceptSelf([-1, 1, 0, -3, 3])
        )
    )


if __name__ == "__main__":
    main()

"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

"""

from format_utils import format_solution


class Solution:
    def removeStars(self, s: str) -> str:
        newStr = ""
        for char in s:
            if char != "*":
                newStr += char
                continue
            if len(newStr) > 0:
                newStr = newStr[:-1]
        return newStr


if __name__ == "__main__":
    sol = Solution()
    input = "leet**cod*e"
    expected = "lecoe"
    print(format_solution(input, expected, sol.removeStars(input)))

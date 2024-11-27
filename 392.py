"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS == lenT:
            return s == t
        x = 0
        y = 0
        for charS in s:
            for i in range(y, lenT):
                if t[i] == charS:
                    x += 1
                    y = i + 1
                    break

        return x == lenS


def main():
    sol = Solution()
    print(f"expected true, {sol.isSubsequence("abc", "ahbgdc")}")
    print(f"expected false, {sol.isSubsequence("axc", "ahbgdc")}")
    print(f"expected True, {sol.isSubsequence("", "ahbgdc")}")
    print(f"expected true, {sol.isSubsequence("abc", "ahbgdc")}")
    print(f"expected false, {sol.isSubsequence("bb", "ahbgdc")}")


if __name__ == "__main__":
    main()

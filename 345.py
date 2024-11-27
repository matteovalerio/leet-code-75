# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution:
    def reverseVowels(self, s: str) -> str:
        # create a list of tuples (index, vowel) and populate it with the vowels contained in the string
        # then replace them in opposite order
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        chars = list(s)
        while left < right:
            while (left < right) and (chars[left] not in vowels):
                left += 1
            while (left < right) and (chars[right] not in vowels):
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]

        return "".join(chars)


def main():
    sol = Solution()

    print(sol.reverseVowels("IceCreAm"))
    print(sol.reverseVowels("leetcode"))


if __name__ == "__main__":
    main()

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words.
# Do not include any extra spaces.


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        currentWord = ""
        for char in s:
            if char == " ":
                if currentWord != "":
                    words.append(currentWord)
                currentWord = ""
            else:
                currentWord += char
        if currentWord != "":
            words.append(currentWord)
        return " ".join(words[::-1])


def main():
    sol = Solution()
    print("expected:")
    print("blue is sky the")
    print("actual")
    print(sol.reverseWords("the sky is blue"))
    print("expected: world hello", "\nactual\n", sol.reverseWords("  hello world  "))
    print("example good a", "\nactual\n", sol.reverseWords("a good   example"))


if __name__ == "__main__":
    main()

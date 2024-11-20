"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        prev_items = [0, 1, 1]
        for x in range(3, n):
            current = prev_items[0] + prev_items[1] + prev_items[2]
            prev_items.pop(0)
            prev_items.append(current)
        return prev_items[0] + prev_items[1] + prev_items[2]


def format_solution(input, expected, actual):
    is_answer_correct = expected == actual
    return f"{'+++' if is_answer_correct else '---'} Input: {input} - Expected: {expected} - Actual: {actual}"


def main():
    sol = Solution()

    print(format_solution(4, 4, sol.tribonacci(4)))
    print(format_solution(25, 1389537, sol.tribonacci(25)))
    print(format_solution(31, 53798080, sol.tribonacci(31)))


if __name__ == "__main__":
    main()

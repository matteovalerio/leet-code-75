"""
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid:
- the absolute value represents its size
- the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet
"""

from typing import List

"""
first approach: brute force
 def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        newList = []
        for asteroid in asteroids:
            if len(newList) == 0:
                newList.append(asteroid)
                continue
            if newList[-1] >= 0:
                if asteroid >= 0:
                    newList.append(asteroid)
                    continue
                if newList[-1] + asteroid > 0:
                    continue
                elif newList[-1] + asteroid == 0:
                    newList.pop()
                else:
                    newList.pop()
                    newList.append(asteroid)
            else:
                if asteroid <= 0:
                    newList.append(asteroid)
                    continue
                if asteroid + newList[-1] > 0:
                    continue
                elif newList[-1] + asteroid == 0:
                    newList.pop()
                else:
                    newList.pop()
                    newList.append(asteroid)
        return newList

Not working, since it just checks if the last element of the list has a different sign
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        let's try a different approach
        create an empty list
        pop element from the current list
        if has different sign from the latest in the new list:
        it means that all elements in the current list has the same sign
        check until we find a number that is major that this
        if we don't find any, empty the list and populate with current
        """
        newList = []
        for asteroid in asteroids:
            if len(newList) == 0 or asteroid > 0 or newList[-1] * asteroid > 0:
                newList.append(asteroid)
                continue
            shouldAdd: bool = True
            while len(newList) > 0:
                if newList[-1] < 0 or newList[-1] + asteroid > 0:
                    break
                elif newList[-1] + asteroid == 0:
                    newList.pop()
                    shouldAdd = False
                    break
                newList.pop()
            if len(newList) == 0 or shouldAdd:
                newList.append(asteroid)
        return newList


def format_solution(input, expected, actual):
    is_answer_correct = expected == actual
    return f"{'+++' if is_answer_correct else '---'} Input: {input} - Expected: {expected} - Actual: {actual}"


if __name__ == "__main__":
    sol = Solution()
    """
    input = [5, 10, -5]
    expected = [5, 10]
    print(format_solution(input, expected, sol.asteroidCollision(input)))
    input = [8, -8]
    expected = []
    print(format_solution(input, expected, sol.asteroidCollision(input)))
    input = [10, 2, -5]
    expected = [10]
    print(format_solution(input, expected, sol.asteroidCollision(input)))
    input = [10, -4, 2, -5]
    expected = [10]
    print(format_solution(input, expected, sol.asteroidCollision(input)))
    """
    input = [-2, -2, 1, -2]
    expected = [-2, -2, -2]
    print(format_solution(input, expected, sol.asteroidCollision(input)))

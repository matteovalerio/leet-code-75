"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

import sys
from typing import List

from format_utils import format_solution


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        il piano è semplice:
        1. creo array che contiene la max distance per ogni valore
        2. itero su ogni elemento, per ognuno calcolo la distance * valore nell'array
        3. trovo il numero più alto nella lista

        ottimizzazione:
        1. resta uguale
        2. itero su ogni elemento, tenendo traccia del numero più piccolo a sinistra del corrente
        3. tengo traccia in una variabile del max number e ritorno quello

        applicazione su array di test [1, 8, 6, 2, 5, 4, 8, 3, 7]
        1.[0,0,0,0,0,0,0,0,0]
        2. 1 > 8 ? no +1
           1 > 6 ? no +1
           ....
           [8*1,0,0,0,0,0,0,0,0]
           8
           [8,0,0,0,0,0,0,0,0]
            6
            6 > 2? si
            6 > 8? no +1
            [8,0,6,0,0,0,0,0,0]


            forse sarebbe meglio
            2a. itero su ogni elemento a destra
            2b. itero su ogni elemento a sinistra e moltiplico
        """
        left, right = 0, len(height) - 1
        maxValue = 0
        while left < right:
            currWidth = right - left
            currHeight = min(height[left], height[right])
            current = currHeight * currWidth
            maxValue = max(current, maxValue)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxValue

        for x in range(len(height)):
            y = x + 1
            bestMatch = x
            for y in range(y, len(height)):
                if height[x] <= height[y]:
                    bestMatch = y
            areas[x] = bestMatch - x
        maxValue = 0
        for x in range(len(height) - 1, -1, -1):
            y = x - 1
            bestMatch = x
            while y >= 0:
                if height[x] <= height[y]:
                    bestMatch = y
                y -= 1
            areas[x] = (areas[x] + (x - bestMatch)) * height[x]
            if areas[x] > maxValue:
                maxValue = areas[x]

        return maxValue


def main():
    sol = Solution()

    res = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    format_solution([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, res)
    res = sol.maxArea([1, 1])
    format_solution([1, 1], 1, res)
    res = sol.maxArea([2, 1])
    format_solution([2, 1], 1, res)


if __name__ == "__main__":
    main()

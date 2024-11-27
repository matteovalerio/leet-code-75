"""
Given an integer array nums,
return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
"""

import math
from typing import List


class Solution:
    def increasingTriplet2(self, nums: List[int]) -> bool:
        first = second = math.inf
        for third in nums:
            if third > second:
                return True
            elif third > first:
                second = third
            else:
                first = third
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        crea lista Tuple [] -> sarà una lista di tuple (indice, valore) che corrispondono alla descrizione del problema
        itera su nums
        se lista Tupla vuota o se l'ultimo numero della lista tupla è < del corrente
            aggiungi (indice, valore) dentro alla lista Tupla
        itera tutta la lista
        se trovo


        [20,100,10,12,5,13]
        [(0, 20)] length == 3 ? no
        20 < 100 ? si
        [(0, 20), (1, 100)]  length == 3 ? no
        100 < 10 ? no
        100 < 12 ? no
        100 < 5 ? no
        100 < 13 ? no
        [(2, 10)]
        10 < 12 ? si
        [(2, 10), (3, 12)]
        12 < 5 ? no
        12 < 13 ? si
        [(2, 10), (3, 12), (4, 13)]  length == 3 ? si -> return
        """
        uniqueSet = set(nums)
        if len(uniqueSet) < 3:
            return False
        increasingTriples = []
        for i in range(len(nums)):
            if len(increasingTriples) == 0:
                increasingTriples.append(i)
            else:
                # it means we didn't find a triplet before
                firstIndex = increasingTriples[0]
                if nums[i] > nums[firstIndex]:
                    continue
                increasingTriples = [i]
            j = i
            for j in range(i, len(nums)):
                increasingTriplesLen = len(increasingTriples)
                currentMaxIndex = increasingTriples[increasingTriplesLen - 1]

                if nums[j] > nums[currentMaxIndex]:
                    if increasingTriplesLen == 2:
                        return True
                    increasingTriples.append((j))
                else:
                    if (
                        increasingTriplesLen == 2
                        and nums[j] > nums[increasingTriples[0]]
                    ):
                        increasingTriples.pop()
                        increasingTriples.append(j)

        return len(increasingTriples) == 3


def main():
    sol = Solution()
    input = [2, 1, 5, 0, 6, 10]
    print(f"Input {input} Output {sol.increasingTriplet(input)} Expected true")
    print(f"Input {input} Output {sol.increasingTriplet2(input)} Expected true")


if __name__ == "__main__":
    main()

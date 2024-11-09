from typing import List

# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        emptyPlots = 0
        for i in range(len(flowerbed)):
            plot = flowerbed[i]
            emptyRight = False
            emptyLeft = True
            if plot == 0:
                emptyLeft = i == 0 or flowerbed[i - 1] == 0
                emptyRight = i == len(flowerbed) -1 or flowerbed[i +1] == 0
                if emptyLeft and emptyRight:
                    flowerbed[i] = 1
                    emptyPlots += 1
        return emptyPlots >= n
    

def main():
    sol = Solution()
    
    res = sol.canPlaceFlowers([1,0,0,0,1], 1)
    print(res) #true
    res = sol.canPlaceFlowers([1,0,0,0,1], 2)
    print(res) # false
    res = sol.canPlaceFlowers([1,0,0,0,0,1], 2)
    print(res) #false

if __name__ == "__main__":
    main()
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if len(flowerbed) == 1:
            if flowerbed[0] and n > 0:
                return False
            else:
                return True

        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2
                continue
            
            else:
                if (
                    (i == 0 and not flowerbed[i + 1])
                    or (i == len(flowerbed) - 1 and not flowerbed[i - 1])
                    or (not flowerbed[i - 1] and not flowerbed[i + 1])
                    ):
                    n -= 1
                    i += 1
            i += 1

        if n > 0:
            return False
        else:
            return True
                
                

         
        
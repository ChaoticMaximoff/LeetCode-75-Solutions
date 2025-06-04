class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        for candy in candies:
            if candy > maxCandy:
                maxCandy = candy
        
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maxCandy)

        return result 
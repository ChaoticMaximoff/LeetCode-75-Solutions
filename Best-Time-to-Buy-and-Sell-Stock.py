class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        profit = 0
        buy = sys.maxsize

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit
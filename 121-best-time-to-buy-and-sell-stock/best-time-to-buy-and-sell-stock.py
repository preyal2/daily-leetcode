class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit from buying and selling a stock once.
        
        Time Complexity: O(n) - single pass through the price array
        Space Complexity: O(1) - constant extra space
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

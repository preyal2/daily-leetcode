class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        State machine dynamic programming tracking max profit through at most 2 buy-sell transactions.

        Time Complexity: O(N) single-pass iteration through prices.
        Space Complexity: O(1) constant auxiliary memory using 4 state variables.
        """
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2

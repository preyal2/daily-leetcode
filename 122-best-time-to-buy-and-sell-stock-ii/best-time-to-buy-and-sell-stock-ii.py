class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Greedy accumulation of all positive price ascents.

        Time Complexity: O(N) single-pass traversal over price array.
        Space Complexity: O(1) constant auxiliary space.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

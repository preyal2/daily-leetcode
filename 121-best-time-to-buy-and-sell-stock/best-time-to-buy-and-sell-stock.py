class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        mi = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            p = prices[i]

            profit = p - mi
            if profit > ans:
                ans = profit

            if p < mi:
                mi = p

        return ans
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ans = 0

        for p in prices[1:]:
            if p < mi:
                mi = p
            elif p - mi > ans:
                ans = p - mi

        return ans
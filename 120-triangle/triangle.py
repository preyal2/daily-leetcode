class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]
            for j in range(i + 1):
                a = dp[j]
                b = dp[j + 1]
                dp[j] = row[j] + (a if a < b else b)

        return dp[0]
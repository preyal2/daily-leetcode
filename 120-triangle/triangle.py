class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Bottom-up dynamic programming computing minimum path sum in O(N) space.

        Time Complexity: O(N^2) where N is number of rows in the triangle.
        Space Complexity: O(N) auxiliary space using 1D DP array.
        """
        dp = list(triangle[-1])
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]

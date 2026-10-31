class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 1_000_000_007
        n = len(grid[0])

        dp = [0] * n
        dp[0] = 1

        for row in grid:
            left = 0

            for j, cell in enumerate(row):
                above = dp[j]

                if cell:
                    dp[j] = left
                    left = above
                else:
                    total = left + above
                    if total >= MOD:
                        total -= MOD

                    dp[j] = total
                    left = total

        return left
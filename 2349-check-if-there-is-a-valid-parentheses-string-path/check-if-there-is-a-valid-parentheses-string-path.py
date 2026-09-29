class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid path must contain an even number of characters.
        if (m + n - 1) & 1:
            return False

        # First character must be '(' and last must be ')'.
        if grid[0][0] != '(' or grid[m - 1][n - 1] != ')':
            return False

        # dp[j] = bitset of reachable balances at current row.
        dp = [0] * n

        for i in range(m):
            left = 0

            for j in range(n):
                c = grid[i][j]

                if i == 0 and j == 0:
                    cur = 1
                else:
                    cur = dp[j] | left

                if c == '(':
                    cur <<= 1
                else:
                    cur >>= 1

                dp[j] = cur
                left = cur

                if cur == 0:
                    dp[j] = 0
                    left = 0

        return bool(dp[-1] & 1)
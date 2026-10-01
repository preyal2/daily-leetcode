class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        if n == 0:
            return 1
        if len(s) < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for c in s:
            for j in range(n - 1, -1, -1):
                if c == t[j]:
                    dp[j + 1] += dp[j]

        return dp[n]
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = list(range(-1, n))

        for c in range(n):
            # Odd-length palindromes
            l = r = c
            while l >= 0 and r < n and s[l] == s[r]:
                v = dp[l] + 1
                if v < dp[r + 1]:
                    dp[r + 1] = v
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = c, c + 1
            while l >= 0 and r < n and s[l] == s[r]:
                v = dp[l] + 1
                if v < dp[r + 1]:
                    dp[r + 1] = v
                l -= 1
                r += 1

        return dp[n]
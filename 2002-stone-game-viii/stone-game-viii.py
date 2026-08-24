class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        prefix = [0] * n
        s = 0

        for i, x in enumerate(stones):
            s += x
            prefix[i] = s

        dp = prefix[-1]

        for i in range(n - 3, -1, -1):
            dp = max(dp, prefix[i + 1] - dp)

        return dp
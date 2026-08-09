from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @cache
        def dfs(i, m):
            if (m << 1) >= n - i:
                return suffix[i]

            total = suffix[i]
            best = 0

            for x in range(1, (m << 1) + 1):
                current = total - dfs(i + x, max(m, x))

                if current > best:
                    best = current

            return best

        return dfs(0, 1)
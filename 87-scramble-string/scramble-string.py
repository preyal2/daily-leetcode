from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if s1 == s2:
            return True

        # Prefix counts for O(26) substring-anagram checks.
        p1 = [[0] * 26 for _ in range(n + 1)]
        p2 = [[0] * 26 for _ in range(n + 1)]

        for i in range(n):
            a = ord(s1[i]) - 97
            b = ord(s2[i]) - 97

            p1[i + 1] = p1[i].copy()
            p2[i + 1] = p2[i].copy()

            p1[i + 1][a] += 1
            p2[i + 1][b] += 1

        def same_chars(i, j, k):
            a = p1
            b = p2
            x1 = a[i]
            x2 = a[i + k]
            y1 = b[j]
            y2 = b[j + k]

            for c in range(26):
                if x2[c] - x1[c] != y2[c] - y1[c]:
                    return False
            return True

        @cache
        def dfs(i, j, k):
            if k == 1:
                return s1[i] == s2[j]

            if s1[i:i + k] == s2[j:j + k]:
                return True

            if not same_chars(i, j, k):
                return False

            # Try smaller pieces first.
            end = k - 1

            for h in range(1, k):
                # No swap
                if dfs(i, j, h) and dfs(i + h, j + h, k - h):
                    return True

                # Swap
                if dfs(i, j + k - h, h) and dfs(i + h, j, k - h):
                    return True

            return False

        return dfs(0, 0, n)
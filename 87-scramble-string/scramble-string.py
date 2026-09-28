from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if s1 == s2:
            return True

        freq1 = {}
        freq2 = {}

        for i, c in enumerate(s1):
            freq1.setdefault(c, []).append(i)

        @cache
        def dfs(i, j, k):
            if s1[i:i + k] == s2[j:j + k]:
                return True

            if k == 1:
                return False

            # Quick exact frequency check.
            c1 = [0] * 26
            c2 = [0] * 26

            for p in range(i, i + k):
                c1[ord(s1[p]) - 97] += 1

            for p in range(j, j + k):
                c2[ord(s2[p]) - 97] += 1

            if c1 != c2:
                return False

            for h in range(1, k):
                if dfs(i, j, h) and dfs(i + h, j + h, k - h):
                    return True

                if dfs(i, j + k - h, h) and dfs(i + h, j, k - h):
                    return True

            return False

        return dfs(0, 0, n)
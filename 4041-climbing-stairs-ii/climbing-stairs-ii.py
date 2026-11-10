class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        a, b, c = 0, 0, 0

        for i, x in enumerate(costs, 1):
            best = a + 1

            if i > 1:
                v = b + 4
                if v < best:
                    best = v

            if i > 2:
                v = c + 9
                if v < best:
                    best = v

            c, b, a = b, a, best + x

        return a
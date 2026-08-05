class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        r = x
        while r > x // r:
            r = (r + x // r) >> 1

        return r
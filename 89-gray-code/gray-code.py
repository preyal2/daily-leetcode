class Solution:
    def grayCode(self, n: int) -> list[int]:
        N = 1 << n
        return [i ^ (i >> 1) for i in range(N)]
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = [x * x for x in nums]
        a.sort()
        m = len(a) >> 1
        return sum(a[m:]) - sum(a[:m])
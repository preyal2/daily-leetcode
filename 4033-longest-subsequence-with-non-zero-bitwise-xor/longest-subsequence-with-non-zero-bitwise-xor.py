class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor = 0
        has_nonzero = False

        for x in nums:
            xor ^= x
            if x:
                has_nonzero = True

        if not has_nonzero:
            return 0

        return len(nums) if xor else len(nums) - 1
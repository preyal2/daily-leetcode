class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Space-optimized O(1) dynamic programming for maximum non-adjacent subarray sum.

        Time Complexity: O(N) single-pass iteration through houses.
        Space Complexity: O(1) constant auxiliary space using two pointers.
        """
        prev1 = 0  # max profit robbing up to i-1
        prev2 = 0  # max profit robbing up to i-2

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1

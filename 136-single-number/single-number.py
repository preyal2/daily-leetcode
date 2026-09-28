class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the unique non-paired element using bitwise XOR cancellation property.

        Time Complexity: O(N) single-pass iteration.
        Space Complexity: O(1) constant auxiliary space.
        """
        result = 0
        for num in nums:
            result ^= num
        return result

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Bitwise state machine tracking modulo-3 occurrences with two state bitmasks.

        Time Complexity: O(N) single pass over nums.
        Space Complexity: O(1) constant auxiliary storage.
        """
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

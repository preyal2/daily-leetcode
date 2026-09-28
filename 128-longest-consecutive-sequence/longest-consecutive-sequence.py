class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Finds length of longest consecutive element sequence in linear time via Hash Set.

        Time Complexity: O(N) each element is visited at most twice.
        Space Complexity: O(N) hash set auxiliary storage.
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if num is the beginning of a streak
            if num - 1 not in num_set:
                current_num = num
                streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    streak += 1
                if streak > longest:
                    longest = streak

        return longest

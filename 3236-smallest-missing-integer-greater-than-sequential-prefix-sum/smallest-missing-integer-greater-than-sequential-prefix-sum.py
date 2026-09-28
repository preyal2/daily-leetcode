class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        """
        Finds the smallest integer >= sum of the longest sequential prefix missing from nums.

        Time Complexity: O(N) to compute the sequential prefix sum and create the hash set.
        Space Complexity: O(N) auxiliary space to store unique numbers in a hash set.
        """
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        num_set = set(nums)
        candidate = prefix_sum
        while candidate in num_set:
            candidate += 1

        return candidate

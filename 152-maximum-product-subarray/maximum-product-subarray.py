class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Dynamic programming tracking running min and max products to handle negative multipliers.

        Time Complexity: O(N) single-pass iteration.
        Space Complexity: O(1) constant auxiliary space.
        """
        if not nums:
            return 0

        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            if max_prod > result:
                result = max_prod

        return result

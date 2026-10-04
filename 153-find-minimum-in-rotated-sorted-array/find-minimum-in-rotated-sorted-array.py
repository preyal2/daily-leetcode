class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Modified binary search isolating rotation inflection pivot.

        Time Complexity: O(log N) logarithmic binary search.
        Space Complexity: O(1) constant auxiliary space.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

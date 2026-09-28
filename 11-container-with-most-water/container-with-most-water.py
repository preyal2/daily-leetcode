class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Calculates the maximum water container area using the two-pointer inward-convergence technique.

        Time Complexity: O(N) where N is the length of height. Each pointer moves at most N times.
        Space Complexity: O(1) auxiliary space as only two integer pointers are maintained.
        """
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            current_area = width * h
            if current_area > max_water:
                max_water = current_area

            # Move pointer with smaller height inward to potentially find a taller boundary
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

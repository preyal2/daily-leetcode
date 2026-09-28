class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Generates all permutations using in-place backtracking with element swaps.

        Time Complexity: O(N * N!) since there are N! permutations, each of length N.
        Space Complexity: O(N) recursion stack depth (excluding the output array).
        """
        result = []
        n = len(nums)

        def backtrack(start: int):
            if start == n:
                result.append(nums[:])
                return

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result

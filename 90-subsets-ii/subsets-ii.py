class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        Generates unique subsets with duplicate pruning after sorting.

        Time Complexity: O(N * 2^N) generating at most 2^N subsets of length up to N.
        Space Complexity: O(N) recursion call stack depth.
        """
        nums.sort()
        res = []
        path = []

        def backtrack(start: int):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res

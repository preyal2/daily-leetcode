class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Two-pass greedy distribution satisfying local slope constraints in linear time.

        Time Complexity: O(N) where N is the number of children.
        Space Complexity: O(N) auxiliary array storing candy counts per child.
        """
        n = len(ratings)
        candies = [1] * n

        # Left-to-right pass: satisfy left neighbor constraint
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left pass: satisfy right neighbor constraint
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

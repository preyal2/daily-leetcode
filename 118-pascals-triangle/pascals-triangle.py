class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        Generates the first numRows of Pascal's triangle dynamically.

        Time Complexity: O(numRows^2) calculating each element once.
        Space Complexity: O(1) auxiliary space (excluding result structure).
        """
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle

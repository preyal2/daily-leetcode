class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        Computes rowIndex-th row of Pascal's triangle in O(rowIndex) auxiliary memory.

        Time Complexity: O(rowIndex^2) in-place reverse summation.
        Space Complexity: O(rowIndex) auxiliary space for the output row.
        """
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row

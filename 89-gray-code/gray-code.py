class Solution:
    def grayCode(self, n: int) -> list[int]:
        """
        Generates n-bit Gray code sequence using formula: G(i) = i ^ (i >> 1).

        Time Complexity: O(2^N) generating 2^N elements.
        Space Complexity: O(1) auxiliary space (excluding result array).
        """
        return [i ^ (i >> 1) for i in range(1 << n)]

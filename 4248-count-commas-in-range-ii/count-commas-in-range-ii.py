class Solution:
    def countCommas(self, n: int) -> int:
        """
        Calculates the total number of commas used when writing all integers from 1 to n.

        Time Complexity: O(log1000 N) <= 5 iterations for N <= 10^15.
        Space Complexity: O(1) constant auxiliary memory.
        """
        total = 0
        threshold = 1000

        while n >= threshold:
            total += (n - threshold + 1)
            threshold *= 1000

        return total

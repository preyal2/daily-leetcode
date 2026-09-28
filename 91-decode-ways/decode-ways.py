class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Computes valid message decodings using O(1) space bottom-up dynamic programming.

        Time Complexity: O(N) single-pass iteration through string length N.
        Space Complexity: O(1) auxiliary space using two state variables.
        """
        if not s or s[0] == '0':
            return 0

        prev2 = 1  # dp[i-2]
        prev1 = 1  # dp[i-1]

        for i in range(1, len(s)):
            curr = 0
            # Single digit decode
            if s[i] != '0':
                curr += prev1

            # Two digit decode
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Determines string segmentability using bottom-up dynamic programming.

        Time Complexity: O(N^2) where N is length of string s.
        Space Complexity: O(N + M) for boolean DP table and dictionary hash set.
        """
        word_set = set(wordDict)
        max_len = max(len(w) for w in wordDict) if wordDict else 0
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

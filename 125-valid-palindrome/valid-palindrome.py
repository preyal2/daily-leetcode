class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        In-place bidirectional two-pointer verification of alphanumeric palindrome.

        Time Complexity: O(N) single pass traversing string s.
        Space Complexity: O(1) auxiliary space without extra strings.
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

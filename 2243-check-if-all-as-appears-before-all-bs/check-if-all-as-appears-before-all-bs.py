class Solution:
    def checkString(self, s: str) -> bool:
        """
        Checks if every 'a' appears before every 'b' in the string s.
        An invalid state occurs if and only if 'ba' exists as a substring.

        Complexity:
            Time: O(N) where N is the length of s.
            Space: O(1) auxiliary space.
        """
        return "ba" not in s

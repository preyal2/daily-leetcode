class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        Backtracking with memoized palindrome validation for all valid partition cuts.

        Time Complexity: O(N * 2^N) in worst case generating partitions of length N.
        Space Complexity: O(N) recursion call stack depth.
        """
        result = []
        path = []
        n = len(s)

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if is_palindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result

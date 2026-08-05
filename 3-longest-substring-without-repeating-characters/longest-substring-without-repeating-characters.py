class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        left = 0
        ans = 0

        for right in range(len(s)):
            idx = ord(s[right])

            if last[idx] >= left:
                left = last[idx] + 1

            last[idx] = right

            length = right - left + 1
            if length > ans:
                ans = length

        return ans
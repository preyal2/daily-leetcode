class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = {}
        ans = left = 0

        for right, x in enumerate(nums):
            cnt[x] = cnt.get(x, 0) + 1

            while cnt[x] > k:
                y = nums[left]
                cnt[y] -= 1
                left += 1

            cur = right - left + 1
            if cur > ans:
                ans = cur

        return ans
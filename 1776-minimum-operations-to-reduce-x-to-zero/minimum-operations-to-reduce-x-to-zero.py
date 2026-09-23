class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1
        if target == 0:
            return n

        left = 0
        cur = 0
        longest = -1

        for right, v in enumerate(nums):
            cur += v

            while cur > target:
                cur -= nums[left]
                left += 1

            if cur == target:
                length = right - left + 1
                if length > longest:
                    longest = length

        return -1 if longest == -1 else n - longest
class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n - l + 1):
            total = 0
            end = min(n, i + r)

            for j in range(i, end):
                total += nums[j]

                if j - i + 1 >= l and total > 0:
                    if ans == 0 or total < ans:
                        ans = total

        return ans if ans else -1
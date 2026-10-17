class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)
        order = sorted((digit_sum(x), x) for x in nums)
        target = {num: i for i, (_, num) in enumerate(order)}

        seen = [False] * n
        ans = 0

        for i, num in enumerate(nums):
            if seen[i] or target[num] == i:
                continue

            cycle = 0
            j = i

            while not seen[j]:
                seen[j] = True
                j = target[nums[j]]
                cycle += 1

            ans += cycle - 1

        return ans
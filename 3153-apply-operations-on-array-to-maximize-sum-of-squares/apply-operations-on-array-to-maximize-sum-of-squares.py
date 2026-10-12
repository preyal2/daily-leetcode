class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        cnt = [0] * 31

        for x in nums:
            while x:
                bit = x & -x
                cnt[bit.bit_length() - 1] += 1
                x ^= bit

        ans = 0
        for _ in range(k):
            x = 0
            for i in range(30, -1, -1):
                if cnt[i]:
                    x |= 1 << i
                    cnt[i] -= 1
            ans = (ans + x * x) % MOD

        return ans
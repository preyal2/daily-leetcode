class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        k = k1 + k2

        if k == 0:
            return sum((a - b) ** 2 for a, b in zip(nums1, nums2))

        cnt = [0] * 100001
        total = sq = mx = 0

        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            cnt[d] += 1
            total += d
            sq += d * d
            if d > mx:
                mx = d

        if total <= k:
            return 0

        for v in range(mx, 0, -1):
            c = cnt[v]
            if c:
                take = c if c < k else k

                # Reducing v to v-1 decreases its square by 2*v-1.
                sq -= take * (2 * v - 1)
                k -= take

                cnt[v] -= take
                cnt[v - 1] += take

                if k == 0:
                    break

        return sq
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        size = n * 4

        lazy = [0] * size
        sums = [0] * size
        sq = [0] * size

        def update(i, lo, hi, ql, qr):
            if ql <= lo and hi <= qr:
                length = hi - lo + 1
                old = sums[i]
                sq[i] = (sq[i] + 2 * old + length) % MOD
                sums[i] = (old + length) % MOD
                lazy[i] += 1
                return

            pending = lazy[i]
            mid = (lo + hi) >> 1
            left = (i << 1) + 1
            right = left + 1

            if pending:
                length = mid - lo + 1
                old = sums[left]
                sq[left] = (sq[left] + 2 * pending * old
                            + pending * pending * length) % MOD
                sums[left] = (old + pending * length) % MOD
                lazy[left] += pending

                length = hi - mid
                old = sums[right]
                sq[right] = (sq[right] + 2 * pending * old
                             + pending * pending * length) % MOD
                sums[right] = (old + pending * length) % MOD
                lazy[right] += pending

                lazy[i] = 0

            if ql <= mid:
                update(left, lo, mid, ql, qr)

            if qr > mid:
                update(right, mid + 1, hi, ql, qr)

            sums[i] = (sums[left] + sums[right]) % MOD
            sq[i] = (sq[left] + sq[right]) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            l = last.get(x, -1) + 1
            update(0, 0, n - 1, l, r)
            last[x] = r
            ans = (ans + sq[0]) % MOD

        return ans
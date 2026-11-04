from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        if k == 0:
            return 0

        # Coordinate compression
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        size = len(vals)

        # Fenwick trees for frequencies and sums
        bit_count = [0] * (size + 1)
        bit_sum = [0] * (size + 1)

        def update(i, dc, ds):
            while i <= size:
                bit_count[i] += dc
                bit_sum[i] += ds
                i += i & -i

        def prefix(i):
            count = total = 0
            while i:
                count += bit_count[i]
                total += bit_sum[i]
                i -= i & -i
            return count, total

        # Find the zero-based compressed index of kth smallest.
        def kth_smallest(kth):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= size and bit_count[nxt] < kth:
                    idx = nxt
                    kth -= bit_count[nxt]
                step >>= 1

            return idx

        # Calculate minimum cost for every window of size x.
        min_ops = []
        window_sum = 0
        median_rank = (x + 1) // 2

        for i, v in enumerate(nums):
            update(rank[v], 1, v)
            window_sum += v

            if i >= x:
                old = nums[i - x]
                update(rank[old], -1, -old)
                window_sum -= old

            if i >= x - 1:
                mid_idx = kth_smallest(median_rank)
                median = vals[mid_idx]

                lower_count, lower_sum = prefix(mid_idx + 1)

                upper_count = x - lower_count
                upper_sum = window_sum - lower_sum

                cost = (
                    median * lower_count - lower_sum
                    + upper_sum - median * upper_count
                )

                min_ops.append(cost)

        # DP: minimum cost to select exactly j non-overlapping windows.
        INF = 10**30

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for end in range(x, n + 1):
                skip = curr[end - 1]
                pick = prev[end - x] + min_ops[end - x]

                curr[end] = skip if skip < pick else pick

            prev = curr

        return prev[n]
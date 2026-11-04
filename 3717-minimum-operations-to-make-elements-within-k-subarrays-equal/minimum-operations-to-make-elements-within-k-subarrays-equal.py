from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        if k == 0:
            return 0

        INF = (1 << 62) - 1

        if k * x > n:
            return INF

        # Coordinate compression
        vals = sorted(set(nums))
        size = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}
        ids = [rank[v] for v in nums]

        # Fenwick trees
        bc = [0] * (size + 1)
        bs = [0] * (size + 1)

        add_count = bc
        add_sum = bs

        # Sliding window median costs
        costs = []
        window_sum = 0
        median_rank = (x + 1) >> 1
        top = 1 << (size.bit_length() - 1)

        for i, v in enumerate(nums):
            p = ids[i]

            while p <= size:
                add_count[p] += 1
                add_sum[p] += v
                p += p & -p

            window_sum += v

            if i >= x:
                old = nums[i - x]
                p = ids[i - x]

                window_sum -= old

                while p <= size:
                    add_count[p] -= 1
                    add_sum[p] -= old
                    p += p & -p

            if i >= x - 1:
                # Find median and sum of the smallest median_rank values.
                idx = 0
                need = median_rank
                lower_sum = 0
                step = top

                while step:
                    nxt = idx + step

                    if nxt <= size and bc[nxt] < need:
                        need -= bc[nxt]
                        lower_sum += bs[nxt]
                        idx = nxt

                    step >>= 1

                median = vals[idx]
                lower_sum += median * need

                upper_sum = window_sum - lower_sum
                upper_count = x - median_rank

                cost = (
                    median * median_rank - lower_sum
                    + upper_sum - median * upper_count
                )

                costs.append(cost)

        # DP with two reusable arrays.
        prev = [0] * (n + 1)
        curr = [INF] * (n + 1)

        for j in range(1, k + 1):
            limit = n - j * x
            curr[limit + 1] = INF

            for i in range(limit, -1, -1):
                skip = curr[i + 1]
                pick = costs[i] + prev[i + x]

                curr[i] = pick if pick < skip else skip

            prev, curr = curr, prev

        return prev[0]
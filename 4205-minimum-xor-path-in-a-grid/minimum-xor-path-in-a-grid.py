class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        bits = max(max(row) for row in grid).bit_length()
        mx = 1 << bits

        # Masks that swap bit positions differing in one XOR-index bit.
        all_mask = (1 << mx) - 1
        low_masks = []
        high_masks = []
        shifts = []

        for p in range(bits):
            block = 1 << p
            low = all_mask // ((1 << block) + 1)
            low_masks.append(low)
            high_masks.append(low << block)
            shifts.append(block)

        dp = [0] * n

        for i, row in enumerate(grid):
            left = 0

            for j, x in enumerate(row):
                if i == 0 and j == 0:
                    cur = 1 << x
                else:
                    cur = dp[j] | left
                    value = x

                    while value:
                        bit = value & -value
                        p = bit.bit_length() - 1

                        cur = (
                            ((cur & low_masks[p]) << shifts[p])
                            | ((cur & high_masks[p]) >> shifts[p])
                        )

                        value ^= bit

                dp[j] = cur
                left = cur

        # Position of the lowest set bit = minimum reachable XOR.
        result = dp[-1]
        return (result & -result).bit_length() - 1
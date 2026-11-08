class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows = [sum(row) for row in grid]
        cols = [0] * n

        for row in grid:
            for j, v in enumerate(row):
                cols[j] += v

        ans = sum(rows)

        for i in range(m):
            if rows[i] == 1:
                j = grid[i].index(1)
                if cols[j] == 1:
                    ans -= 1

        return ans
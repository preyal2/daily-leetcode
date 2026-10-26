class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                total = grid[i][j]
                if total == 0:
                    continue

                grid[i][j] = 0
                stack = [(i, j)]

                while stack:
                    x, y = stack.pop()

                    if x > 0:
                        v = grid[x - 1][y]
                        if v:
                            total += v
                            grid[x - 1][y] = 0
                            stack.append((x - 1, y))

                    if x + 1 < m:
                        v = grid[x + 1][y]
                        if v:
                            total += v
                            grid[x + 1][y] = 0
                            stack.append((x + 1, y))

                    if y > 0:
                        v = grid[x][y - 1]
                        if v:
                            total += v
                            grid[x][y - 1] = 0
                            stack.append((x, y - 1))

                    if y + 1 < n:
                        v = grid[x][y + 1]
                        if v:
                            total += v
                            grid[x][y + 1] = 0
                            stack.append((x, y + 1))

                if total % k == 0:
                    ans += 1

        return ans
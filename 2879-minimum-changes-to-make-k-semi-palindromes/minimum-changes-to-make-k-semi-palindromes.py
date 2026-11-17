class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9

        # Precompute minimum semi-palindrome cost.
        g = [[INF] * (n + 1) for _ in range(n)]

        for d in range(1, n // 2 + 1):
            prev2 = [0] * (n + 1)
            prev1 = [0] * (n + 1)

            for q in range(2, n // d + 1):
                length = q * d
                limit = n - length + 1
                offset = (q - 1) * d

                cur = [0] * limit

                for i in range(limit):
                    cost = prev2[i + d]

                    a = i
                    b = i + offset

                    for _ in range(d):
                        cost += s[a] != s[b]
                        a += 1
                        b += 1

                    cur[i] = cost

                    end = i + length
                    if cost < g[i][end]:
                        g[i][end] = cost

                prev2, prev1 = prev1, cur

        # DP using two rolling arrays.
        prev = [INF] * (n + 1)
        prev[0] = 0

        for groups in range(1, k + 1):
            curr = [INF] * (n + 1)
            min_start = (groups - 1) * 2

            for end in range(groups * 2, n + 1):
                best = INF

                for start in range(min_start, end - 1):
                    val = prev[start] + g[start][end]

                    if val < best:
                        best = val

                curr[end] = best

            prev = curr

        return prev[n]
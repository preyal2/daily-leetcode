class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:

        logs.sort(key=lambda a: a[1])

        m = len(logs)
        q = len(queries)

        freq = [0] * (n + 1)
        ans = [0] * q

        order = sorted(range(q), key=queries.__getitem__)

        left = right = active = 0

        for idx in order:
            r = queries[idx]
            l = r - x

            while right < m and logs[right][1] <= r:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < l:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
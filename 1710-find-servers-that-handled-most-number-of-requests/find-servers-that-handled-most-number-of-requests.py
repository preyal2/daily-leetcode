from heapq import heappop, heappush
from typing import List


class Solution:
    def busiestServers(
        self, k: int, arrival: List[int], load: List[int]
    ) -> List[int]:

        # Initially every server is available.
        bit = [0] + [i & -i for i in range(1, k + 1)]

        busy = []
        count = [0] * k
        available = k

        pop = heappop
        push = heappush

        highest = 1 << (k.bit_length() - 1)

        for i, (start, duration) in enumerate(zip(arrival, load)):

            # Release servers whose tasks have finished.
            while busy and busy[0][0] <= start:
                _, server = pop(busy)

                p = server + 1
                while p <= k:
                    bit[p] += 1
                    p += p & -p

                available += 1

            if available == 0:
                continue

            # Count available servers before the preferred server.
            p = i % k
            before = 0

            while p:
                before += bit[p]
                p -= p & -p

            # Find the next available server, wrapping around.
            rank = before + 1 if before < available else 1

            # Fenwick tree: find the server with this available rank.
            idx = 0
            step = highest
            r = rank

            while step:
                nxt = idx + step
                if nxt <= k and bit[nxt] < r:
                    idx = nxt
                    r -= bit[nxt]
                step >>= 1

            server = idx

            # Mark server as busy.
            p = server + 1
            while p <= k:
                bit[p] -= 1
                p += p & -p

            available -= 1
            count[server] += 1

            push(busy, (start + duration, server))

        mx = max(count)
        return [i for i, v in enumerate(count) if v == mx]
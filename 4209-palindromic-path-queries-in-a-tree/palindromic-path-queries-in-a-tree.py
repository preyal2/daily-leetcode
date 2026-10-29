from typing import List


class Solution:
    def palindromePath(
        self,
        n: int,
        edges: List[List[int]],
        s: str,
        queries: List[str]
    ) -> List[bool]:

        # Build adjacency list.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # One bit per character.
        char_mask = [1 << (ord(c) - 97) for c in s]

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        # Iterative DFS: Euler tour, depths, parents and root-prefix XOR.
        timer = 0
        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state:
                tout[u] = timer - 1
                continue

            parent[u] = p
            if u:
                depth[u] = depth[p] + 1

            tin[u] = timer
            timer += 1
            prefix[u] = prefix[p] ^ char_mask[u]

            stack.append((u, p, 1))

            for v in reversed(graph[u]):
                if v != p:
                    stack.append((v, u, 0))

        # Binary lifting table for LCA.
        LOG = n.bit_length()
        up = [parent]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for bit in range(LOG - 1, -1, -1):
                a = up[bit][u]
                b = up[bit][v]

                if a != b:
                    u, v = a, b

            return parent[u]

        # Fenwick tree for range-XOR updates and point queries.
        bit = [0] * (n + 1)

        def add(i, value):
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def point(i):
            i += 1
            value = 0

            while i:
                value ^= bit[i]
                i -= i & -i

            return value

        ans = []

        for query in queries:
            op, a, b = query.split()
            u = int(a)

            if op == "update":
                new_mask = 1 << (ord(b) - 97)
                delta = char_mask[u] ^ new_mask

                if delta:
                    # Toggle this character's contribution throughout
                    # the updated node's subtree.
                    add(tin[u] + 1, delta)

                    end = tout[u] + 2
                    if end <= n:
                        add(end, delta)

                    char_mask[u] = new_mask

            else:
                v = int(b)
                p = lca(u, v)

                # Current root-to-node masks after all updates.
                mask_u = prefix[u] ^ point(tin[u])
                mask_v = prefix[v] ^ point(tin[v])

                # Inclusive path mask: add the LCA's character once.
                path_mask = mask_u ^ mask_v ^ char_mask[p]

                # At most one character may have an odd frequency.
                ans.append(path_mask.bit_count() <= 1)

        return ans
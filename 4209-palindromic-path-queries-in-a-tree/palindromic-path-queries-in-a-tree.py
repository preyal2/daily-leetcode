from typing import List


class Solution:
    def palindromePath(
        self,
        n: int,
        edges: List[List[int]],
        s: str,
        queries: List[str]
    ) -> List[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        char_mask = [1 << (ord(c) - 97) for c in s]
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        prefix = [0] * n

        # Iterative DFS and Euler preorder.
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)

            if u == 0:
                prefix[u] = char_mask[u]
            else:
                prefix[u] = prefix[parent[u]] ^ char_mask[u]

            for v in reversed(graph[u]):
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        # Compute subtree sizes and heavy children.
        size = [1] * n
        heavy = [-1] * n

        for idx in range(n - 1, 0, -1):
            u = order[idx]
            p = parent[u]
            size[p] += size[u]

            h = heavy[p]
            if h == -1 or size[u] > size[h]:
                heavy[p] = u

        # Assign HLD chain heads.
        head = [0] * n

        for u in order:
            if u:
                p = parent[u]
                head[u] = head[p] if heavy[p] == u else u

        def lca(u, v):
            while head[u] != head[v]:
                hu = head[u]
                hv = head[v]

                if depth[hu] > depth[hv]:
                    u = parent[hu]
                else:
                    v = parent[hv]

            return u if depth[u] < depth[v] else v

        # Fenwick tree: subtree range-XOR updates, point queries.
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
        append = ans.append

        for query in queries:
            op, a, b = query.split()
            u = int(a)

            if op == "update":
                new_mask = 1 << (ord(b) - 97)
                delta = char_mask[u] ^ new_mask

                if delta:
                    add(tin[u] + 1, delta)

                    end = tin[u] + size[u] + 1
                    if end <= n:
                        add(end, delta)

                    char_mask[u] = new_mask

            else:
                v = int(b)
                p = lca(u, v)

                mask_u = prefix[u] ^ point(tin[u])
                mask_v = prefix[v] ^ point(tin[v])
                path_mask = mask_u ^ mask_v ^ char_mask[p]

                append(path_mask.bit_count() <= 1)

        return ans
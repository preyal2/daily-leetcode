from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        seen = [False] * n
        seen[k] = True

        q = deque([k])

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)

        ans = []

        for u in range(n):
            if seen[u]:
                continue

            for v in graph[u]:
                if seen[v]:
                    return list(range(n))

            ans.append(u)

        return ans
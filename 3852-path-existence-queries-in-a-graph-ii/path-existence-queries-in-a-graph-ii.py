import bisect

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: list[int],
        maxDiff: int,
        queries: list[list[int]]
    ) -> list[int]:
        """
        Computes minimum distance between nodes in a diff-bounded graph using binary lifting.

        Time Complexity: O(N log N + Q log N) where N is number of nodes and Q is queries length.
        Space Complexity: O(N log N) for binary lifting jump tables.
        """
        if maxDiff == 0:
            ans = []
            for u, v in queries:
                if u == v:
                    ans.append(0)
                elif nums[u] == nums[v]:
                    ans.append(1)
                else:
                    ans.append(-1)
            return ans

        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        sorted_vals = [p[0] for p in sorted_pairs]

        comp = [0] * n
        comp_id = 0
        for i in range(1, n):
            if sorted_vals[i] - sorted_vals[i - 1] > maxDiff:
                comp_id += 1
            comp[i] = comp_id

        orig_to_sorted = [0] * n
        for s_idx, (val, orig_idx) in enumerate(sorted_pairs):
            orig_to_sorted[orig_idx] = s_idx

        LOG = 18
        up_right = [[i for i in range(n)] for _ in range(LOG)]
        up_left = [[i for i in range(n)] for _ in range(LOG)]

        for i in range(n):
            target_r = sorted_vals[i] + maxDiff
            idx_r = bisect.bisect_right(sorted_vals, target_r) - 1
            up_right[0][i] = idx_r

            target_l = sorted_vals[i] - maxDiff
            idx_l = bisect.bisect_left(sorted_vals, target_l)
            up_left[0][i] = idx_l

        for k in range(1, LOG):
            for i in range(n):
                up_right[k][i] = up_right[k - 1][up_right[k - 1][i]]
                up_left[k][i] = up_left[k - 1][up_left[k - 1][i]]

        def get_distance(su: int, sv: int) -> int:
            if su == sv:
                return 0
            if comp[su] != comp[sv]:
                return -1

            vu, vv = sorted_vals[su], sorted_vals[sv]
            if abs(vu - vv) <= maxDiff:
                return 1

            steps = 0
            curr = su
            if vu < vv:
                for k in range(LOG - 1, -1, -1):
                    nxt = up_right[k][curr]
                    if sorted_vals[nxt] < vv:
                        steps += (1 << k)
                        curr = nxt
                if sorted_vals[up_right[0][curr]] >= vv:
                    return steps + 1
                return steps + 2
            else:
                for k in range(LOG - 1, -1, -1):
                    nxt = up_left[k][curr]
                    if sorted_vals[nxt] > vv:
                        steps += (1 << k)
                        curr = nxt
                if sorted_vals[up_left[0][curr]] <= vv:
                    return steps + 1
                return steps + 2

        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
            elif abs(nums[u] - nums[v]) <= maxDiff:
                results.append(1)
            else:
                su = orig_to_sorted[u]
                sv = orig_to_sorted[v]
                results.append(get_distance(su, sv))

        return results

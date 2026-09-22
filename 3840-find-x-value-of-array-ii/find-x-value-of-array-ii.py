class Node:
    __slots__ = ("remain", "prod")

    def __init__(self, k):
        self.remain = [0] * k
        self.prod = 1


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)

    def query(self, i, j):
        return self._query(0, 0, self.n - 1, i, j)

    def build(self, nums, cur, left, right):
        if left == right:
            self.tree[cur].remain[nums[left]] = 1
            self.tree[cur].prod = nums[left]
            return

        mid = (left + right) >> 1
        self.build(nums, cur * 2 + 1, left, mid)
        self.build(nums, cur * 2 + 2, mid + 1, right)

        self.tree[cur] = self.merge(
            self.tree[cur * 2 + 1],
            self.tree[cur * 2 + 2]
        )

    def _update(self, tree_index, lo, hi, i, val):
        if lo == hi:
            node = self.tree[tree_index]
            for j in range(self.k):
                node.remain[j] = 0
            node.remain[val] = 1
            node.prod = val
            return

        mid = (lo + hi) >> 1

        if i <= mid:
            self._update(tree_index * 2 + 1, lo, mid, i, val)
        else:
            self._update(tree_index * 2 + 2, mid + 1, hi, i, val)

        self.tree[tree_index] = self.merge(
            self.tree[tree_index * 2 + 1],
            self.tree[tree_index * 2 + 2]
        )

    def _query(self, tree_index, lo, hi, i, j):
        if i <= lo and hi <= j:
            return self.tree[tree_index]

        if j < lo or hi < i:
            return Node(self.k)

        mid = (lo + hi) >> 1

        left = self._query(
            tree_index * 2 + 1, lo, mid, i, j
        )
        right = self._query(
            tree_index * 2 + 2, mid + 1, hi, i, j
        )

        return self.merge(left, right)

    def merge(self, left, right):
        k = self.k
        node = Node(k)

        node.prod = (left.prod * right.prod) % k

        for i in range(k):
            node.remain[i] = left.remain[i]

        lp = left.prod
        for i in range(k):
            node.remain[(i * lp) % k] += right.remain[i]

        return node


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:

        for i in range(len(nums)):
            nums[i] %= k

        for query in queries:
            query[1] %= k

        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []

        for query in queries:
            index, value, start, x = query

            tree.update(index, value)

            ans.append(
                tree.query(start, n - 1).remain[x]
            )

        return ans
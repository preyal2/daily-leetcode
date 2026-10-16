class LazySegmentTree:
    __slots__ = ("n", "mod", "lazy", "sums", "squared")

    def __init__(self, n: int, mod: int):
        self.n = n
        self.mod = mod
        size = 4 * n
        self.lazy = [0] * size
        self.sums = [0] * size
        self.squared = [0] * size

    def propagate(self, i: int, l: int, r: int) -> None:
        mod = self.mod
        lazy = self.lazy[i]
        gap = r - l + 1

        self.squared[i] = (
            self.squared[i] + 2 * lazy * self.sums[i] + lazy * lazy * gap
        ) % mod
        self.sums[i] = (self.sums[i] + lazy * gap) % mod

        if l < r:
            left = i * 2 + 1
            right = left + 1
            self.lazy[left] += lazy
            self.lazy[right] += lazy

        self.lazy[i] = 0

    def update_range(self, l: int, r: int) -> None:
        self._update(0, 0, self.n - 1, l, r)

    def _update(self, i: int, start: int, end: int, l: int, r: int) -> None:
        if self.lazy[i]:
            self.propagate(i, start, end)

        if end < l or start > r:
            return

        if start >= l and end <= r:
            self.lazy[i] = 1
            self.propagate(i, start, end)
            return

        mid = (start + end) // 2
        left = i * 2 + 1
        right = left + 1

        self._update(left, start, mid, l, r)
        self._update(right, mid + 1, end, l, r)

        mod = self.mod
        self.sums[i] = (self.sums[left] + self.sums[right]) % mod
        self.squared[i] = (self.squared[left] + self.squared[right]) % mod

    def get_squared_sums(self) -> int:
        return self.squared[0]


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        mod = 1_000_000_007
        n = len(nums)
        tree = LazySegmentTree(n, mod)
        last_seen = {}
        ans = 0

        for r, x in enumerate(nums):
            l = last_seen.get(x, -1) + 1
            tree.update_range(l, r)
            last_seen[x] = r
            ans = (ans + tree.get_squared_sums()) % mod

        return ans
class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        arr = sorted((v, i) for i, v in enumerate(nums))
        ans = [0] * len(nums)

        i = 0
        n = len(arr)

        while i < n:
            j = i + 1
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            idx = [arr[k][1] for k in range(i, j)]
            idx.sort()

            for p, k in enumerate(idx, i):
                ans[k] = arr[p][0]

            i = j

        return ans
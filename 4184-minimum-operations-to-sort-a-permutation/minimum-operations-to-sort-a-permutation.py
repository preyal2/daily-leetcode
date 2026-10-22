class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        ans = n + 3

        # Check forward circular order.
        prev = nums[zero]
        ok = True

        for i in range(zero + 1, n):
            v = nums[i]
            if prev > v:
                ok = False
                break
            prev = v

        if ok:
            for i in range(zero):
                v = nums[i]
                if prev > v:
                    ok = False
                    break
                prev = v

        if ok:
            a = zero
            b = n - zero + 2
            ans = a if a < b else b

        # Check reverse circular order.
        prev = nums[zero]
        ok = True

        for i in range(zero - 1, -1, -1):
            v = nums[i]
            if prev > v:
                ok = False
                break
            prev = v

        if ok:
            for i in range(n - 1, zero, -1):
                v = nums[i]
                if prev > v:
                    ok = False
                    break
                prev = v

        if ok:
            a = zero + 2
            b = n - zero
            candidate = a if a < b else b
            if candidate < ans:
                ans = candidate

        return -1 if ans == n + 3 else ans
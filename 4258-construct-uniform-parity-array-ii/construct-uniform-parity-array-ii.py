class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        mn = 1 << 60

        for x in nums1:
            if x & 1 and x < mn:
                mn = x

        if mn == 1 << 60:
            return True

        return all(x >= mn for x in nums1 if not (x & 1))
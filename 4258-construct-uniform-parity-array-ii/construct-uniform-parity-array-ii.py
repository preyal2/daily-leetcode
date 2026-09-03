class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        mn = float('inf')

        for x in nums1:
            if x & 1 and x < mn:
                mn = x

        if mn == float('inf'):
            return True

        for x in nums1:
            if not (x & 1) and x < mn:
                return False

        return True
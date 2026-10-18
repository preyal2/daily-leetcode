from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Number of ways to interleave left and right elements
            interleave_ways = comb(len(left) + len(right), len(left))
            
            # Combine the results recursively
            return (interleave_ways * dfs(left) * dfs(right)) % MOD

        # Subtract 1 to exclude the original array configuration
        return (dfs(nums) - 1) % MOD
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Generate all combinations of k numbers from [1, n] using optimized backtracking.
        
        Time Complexity: O(k * C(n, k))
        Space Complexity: O(k) for recursion stack and current path
        """
        result = []
        
        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                result.append(path[:])
                return
            
            # Pruning optimization: stop if there aren't enough remaining numbers to fill k elements
            for num in range(start, n - (k - len(path)) + 2):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
                
        backtrack(1, [])
        return result

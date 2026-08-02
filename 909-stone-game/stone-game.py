class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        Determine if Alice can win the stone game.
      
        Alice and Bob take turns picking stones from either end of the array.
        Alice goes first. Both play optimally.
      
        Args:
            piles: List of integers representing stone piles
          
        Returns:
            True if Alice wins (gets more stones than Bob), False otherwise
        """
        from functools import cache
      
        @cache
        def calculate_score_difference(left: int, right: int) -> int:
            """
            Calculate the maximum score difference the current player can achieve.
          
            The score difference represents how many more stones the current player
            can get compared to their opponent when both play optimally.
          
            Args:
                left: Left boundary index of remaining piles
                right: Right boundary index of remaining piles
              
            Returns:
                Maximum score difference achievable by current player
            """
            # Base case: no piles left to pick
            if left > right:
                return 0
          
            # Current player chooses optimally between:
            # 1. Taking left pile: gain piles[left], opponent gets the difference from remaining
            # 2. Taking right pile: gain piles[right], opponent gets the difference from remaining
            take_left = piles[left] - calculate_score_difference(left + 1, right)
            take_right = piles[right] - calculate_score_difference(left, right - 1)
          
            # Return the maximum score difference achievable
            return max(take_left, take_right)
      
        # Alice wins if her score difference is positive
        return calculate_score_difference(0, len(piles) - 1) > 0
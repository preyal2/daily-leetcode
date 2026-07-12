class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer.
        Returns 0 if the reversed integer overflows.
      
        Args:
            x: A 32-bit signed integer
          
        Returns:
            The reversed integer, or 0 if overflow occurs
        """
        result = 0
      
        # Define 32-bit integer boundaries
        MIN_INT = -(2**31)      # -2147483648
        MAX_INT = 2**31 - 1     # 2147483647
      
        while x != 0:
            # Check for potential overflow before multiplying by 10
            # Truncate the boundaries toward zero to match digit extraction
            if result < int(MIN_INT / 10) or result > int(MAX_INT / 10):
                return 0
          
            # Compute the truncated prefix and recover the current digit
            next_x = int(x / 10)
            digit = x - next_x * 10
          
            # Build the reversed number
            result = result * 10 + digit
          
            # Remove the last digit from x
            x = next_x
          
        return result
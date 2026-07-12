class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Regular Expression Matching with '.' and '*'
        '.' matches any single character
        '*' matches zero or more of the preceding element
      
        Args:
            s: The input string to match
            p: The pattern string with regular expression
          
        Returns:
            True if s matches p, False otherwise
        """
        from functools import cache
      
        # Get lengths of input string and pattern
        s_length = len(s)
        p_length = len(p)
      
        @cache
        def match_helper(s_index: int, p_index: int) -> bool:
            """
            Recursively check if substring s[s_index:] matches pattern p[p_index:]
          
            Args:
                s_index: Current index in string s
                p_index: Current index in pattern p
              
            Returns:
                True if the remaining portions match, False otherwise
            """
            # Base case: reached end of pattern
            if p_index >= p_length:
                # Pattern exhausted, check if string is also exhausted
                return s_index == s_length
          
            # Check if next character in pattern is '*' (Kleene star)
            if p_index + 1 < p_length and p[p_index + 1] == '*':
                # Two options with '*':
                # 1. Skip the pattern char and '*' (match 0 occurrences)
                skip_pattern = match_helper(s_index, p_index + 2)
              
                # 2. Match current char and stay at same pattern position (match 1+ occurrences)
                # Only if current position is valid and characters match
                match_current = (s_index < s_length and 
                                (s[s_index] == p[p_index] or p[p_index] == '.') and 
                                match_helper(s_index + 1, p_index))
              
                return skip_pattern or match_current
          
            # Regular character match (no '*' following)
            # Check if current characters match and continue with next positions
            return (s_index < s_length and 
                   (s[s_index] == p[p_index] or p[p_index] == '.') and 
                   match_helper(s_index + 1, p_index + 1))
      
        # Start matching from the beginning of both strings
        return match_helper(0, 0)
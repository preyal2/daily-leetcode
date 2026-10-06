class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_add = 0
        
        for c in s:
            if c == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_add += 1
                    
        return open_brackets + min_add

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ""

        for ch in str(n):
            if ch != '0':
                s += ch

        if s == "":
            return 0

        x = int(s)
        digit_sum = sum(int(ch) for ch in s)

        return x * digit_sum
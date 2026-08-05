class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(a[i]) - 48
                i -= 1
            if j >= 0:
                carry += ord(b[j]) - 48
                j -= 1

            ans.append(chr((carry & 1) + 48))
            carry >>= 1

        return ''.join(reversed(ans))
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s.
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        # A palindrome can have at most one odd-count character.
        odd = -1
        for i in range(26):
            if cnt[i] & 1:
                if odd != -1:
                    return ""
                odd = i

        half_len = n // 2
        half = [x // 2 for x in cnt]

        # ---------------------------------------------------------
        # Check whether target[:half_len] can be used exactly.
        # ---------------------------------------------------------
        rem = half[:]
        ok = True

        for i in range(half_len):
            x = ord(target[i]) - 97
            if rem[x] == 0:
                ok = False
                break
            rem[x] -= 1

        if ok:
            left = target[:half_len]
            mid = "" if n % 2 == 0 else chr(odd + 97)
            candidate = left + mid + left[::-1]

            if candidate > target:
                return candidate

        # ---------------------------------------------------------
        # Find the smallest left half strictly greater than
        # target[:half_len].
        # ---------------------------------------------------------
        for i in range(half_len - 1, -1, -1):

            # Start from all available half characters.
            rem = half[:]

            # The prefix target[:i] must be exactly matched.
            possible = True
            for j in range(i):
                x = ord(target[j]) - 97
                if rem[x] == 0:
                    possible = False
                    break
                rem[x] -= 1

            if not possible:
                continue

            current = ord(target[i]) - 97

            # Pick the smallest character larger than target[i].
            bigger = -1
            for x in range(current + 1, 26):
                if rem[x]:
                    bigger = x
                    break

            if bigger == -1:
                continue

            rem[bigger] -= 1

            # Build the smallest possible remaining suffix.
            suffix = []
            for x in range(26):
                if rem[x]:
                    suffix.append(chr(x + 97) * rem[x])

            left = target[:i] + chr(bigger + 97) + ''.join(suffix)
            mid = "" if n % 2 == 0 else chr(odd + 97)

            return left + mid + left[::-1]

        return ""
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1

        # Prefix frequency of target.
        # Initially contains all target characters.
        pref = [0] * 26
        for c in target:
            pref[ord(c) - 97] += 1

        for i in range(n - 1, -1, -1):
            ti = ord(target[i]) - 97

            # pref now represents target[:i]
            pref[ti] -= 1

            # target[:i] must be constructible from s
            possible = True
            for x in range(26):
                if pref[x] > freq[x]:
                    possible = False
                    break

            if not possible:
                continue

            # Find the smallest available character > target[i]
            bigger = -1
            for x in range(ti + 1, 26):
                if freq[x] > pref[x]:
                    bigger = x
                    break

            if bigger == -1:
                continue

            # Build answer:
            # target[:i] + bigger + smallest possible suffix
            ans = list(target[:i])
            ans.append(chr(bigger + 97))

            # Remove prefix and chosen bigger character
            remain = freq[:]
            for x in range(26):
                remain[x] -= pref[x]

            remain[bigger] -= 1

            # Smallest lexicographical suffix
            for x in range(26):
                if remain[x]:
                    ans.append(chr(x + 97) * remain[x])

            return ''.join(ans)

        return ""
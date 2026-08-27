class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for c in s:
            freq[ord(c) - 97] += 1

        rem = freq[:]
        best_i = -1
        best_c = -1

        # Find the rightmost position where target can be made
        # and we can replace target[i] with a larger character.
        for i, c in enumerate(target):
            x = ord(c) - 97

            # Try to make this position strictly larger.
            for y in range(x + 1, 26):
                if rem[y]:
                    best_i = i
                    best_c = y
                    break

            # Use target[i] for continuing the equal prefix.
            rem[x] -= 1

            # target prefix is impossible from this point onward.
            if rem[x] < 0:
                break

        if best_i == -1:
            return ""

        # Rebuild counts for the best position.
        rem = freq[:]
        for i in range(best_i):
            rem[ord(target[i]) - 97] -= 1

        rem[best_c] -= 1

        # Smallest possible suffix.
        ans = target[:best_i] + chr(best_c + 97)

        for x in range(26):
            if rem[x]:
                ans += chr(x + 97) * rem[x]

        return ans
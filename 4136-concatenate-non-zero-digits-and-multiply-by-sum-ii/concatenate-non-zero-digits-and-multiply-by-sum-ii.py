MOD = 1_000_000_007


class Solution:
    def sumAndMultiply(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:

        n = len(s)
        mod = MOD

        # Prefix:
        # sd[i]   = sum of digits in s[:i]
        # nz[i]   = number of non-zero digits in s[:i]
        # pref[i] = number formed by non-zero digits in s[:i]
        sd = [0] * (n + 1)
        nz = [0] * (n + 1)
        pref = [0] * (n + 1)

        total_sum = 0
        nonzero = 0
        value = 0

        for i, c in enumerate(s, 1):
            d = ord(c) - 48

            total_sum += d
            sd[i] = total_sum

            if d:
                nonzero += 1
                value = (value * 10 + d) % mod

            nz[i] = nonzero
            pref[i] = value

        # Only calculate powers actually needed.
        pow10 = [1] * (nonzero + 1)
        p = 1
        for i in range(1, nonzero + 1):
            p = p * 10 % mod
            pow10[i] = p

        ans = []
        append = ans.append

        for l, r in queries:
            rr = r + 1

            count = nz[rr] - nz[l]
            digit_sum = sd[rr] - sd[l]

            value = pref[rr] - pref[l] * pow10[count] % mod

            # No need for (value % mod) here.
            # Final modulo already normalizes negative values.
            append(value * digit_sum % mod)

        return ans
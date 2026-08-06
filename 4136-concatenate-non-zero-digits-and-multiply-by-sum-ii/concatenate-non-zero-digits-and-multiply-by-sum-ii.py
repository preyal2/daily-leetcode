MOD = 10**9 + 7
MX = 100001

POW10 = [1] * MX
for i in range(1, MX):
    POW10[i] = (POW10[i - 1] * 10) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        sum_d = [0] * (n + 1)
        cnt = [0] * (n + 1)
        pref = [0] * (n + 1)

        mod = MOD
        pow10 = POW10

        for i in range(n):
            d = ord(s[i]) - 48

            sum_d[i + 1] = sum_d[i] + d
            cnt[i + 1] = cnt[i] + (d != 0)

            if d:
                pref[i + 1] = (pref[i] * 10 + d) % mod
            else:
                pref[i + 1] = pref[i]

        ans = []
        append = ans.append

        for l, r in queries:
            nz = cnt[r + 1] - cnt[l]
            digit_sum = sum_d[r + 1] - sum_d[l]

            val = pref[r + 1] - pref[l] * pow10[nz] % mod
            append((val % mod) * digit_sum % mod)

        return ans
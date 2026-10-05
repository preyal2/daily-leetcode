MOD = 1000000007


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        sd = [0] * (n + 1)
        nz = [0] * (n + 1)
        pref = [0] * (n + 1)

        sm = nonzero = value = 0

        # bytes iteration is cheaper than ord() for every character
        for i, d in enumerate(s.encode(), 1):
            d -= 48
            sm += d
            sd[i] = sm

            if d:
                nonzero += 1
                value = (value * 10 + d) % MOD

            nz[i] = nonzero
            pref[i] = value

        # Only powers that can actually be requested are needed.
        pow10 = [1] * (nonzero + 1)
        p = 1
        for i in range(1, nonzero + 1):
            p = p * 10 % MOD
            pow10[i] = p

        q = len(queries)
        ans = [0] * q

        _sd = sd
        _nz = nz
        _pref = pref
        _pow10 = pow10
        mod = MOD

        for i in range(q):
            l, r = queries[i]
            rr = r + 1

            c = _nz[rr] - _nz[l]
            sm = _sd[rr] - _sd[l]
            v = _pref[rr] - _pref[l] * _pow10[c] % mod

            ans[i] = v * sm % mod

        return ans
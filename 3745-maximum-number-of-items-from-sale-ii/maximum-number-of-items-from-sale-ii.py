from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)
        min_price = 10**9
        max_factor = 0

        # Count item types by factor.
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p
            if f > max_factor:
                max_factor = f

        # Count all item types whose factors are multiples of f.
        gain = [0] * (max_factor + 1)

        for f in range(1, max_factor + 1):
            total = 0

            for multiple in range(f, max_factor + 1, f):
                total += freq[multiple]

            gain[f] = total - 1

        # Group profitable bonus purchases by price.
        deals = {}
        limit = min_price * 2

        for f, p in items:
            if p <= limit:
                cnt = gain[f]

                if cnt:
                    deals[p] = deals.get(p, 0) + cnt

        # Buy the cheapest bonus opportunities first.
        ans = 0

        for p in sorted(deals):
            if budget < p:
                break

            take = min(deals[p], budget // p)

            ans += take * 2
            budget -= take * p

        # Spend remaining budget on the cheapest ordinary item.
        ans += budget // min_price

        return ans
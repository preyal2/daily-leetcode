class Solution:
    def candy(self, ratings: list[int]) -> int:
        ans = 1
        up = down = 0
        prev = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                slope = 1
            elif ratings[i] < ratings[i - 1]:
                slope = -1
            else:
                slope = 0

            if (prev > 0 and slope == 0) or (prev < 0 and slope >= 0):
                ans += up * (up + 1) // 2
                ans += down * (down + 1) // 2
                ans += max(up, down)
                up = down = 0

            if slope > 0:
                up += 1
            elif slope < 0:
                down += 1
            else:
                ans += 1

            prev = slope

        ans += up * (up + 1) // 2
        ans += down * (down + 1) // 2
        ans += max(up, down)

        return ans
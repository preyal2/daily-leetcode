class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = cost = 0
        j = n - 1

        qv = []
        qc = []
        head = tail = 0

        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1

            while tail > head and qv[tail - 1] < num:
                tail -= 1
                v = qv.pop()
                c = qc.pop()

                count += c
                cost += (num - v) * c

            qv.append(num)
            qc.append(count)
            tail += 1

            while cost > k:
                v = qv[head]
                c = qc[head]

                cost -= v - nums[j]
                j -= 1

                if c > 1:
                    qc[head] = c - 1
                else:
                    head += 1

            ans += j - i + 1

        return ans
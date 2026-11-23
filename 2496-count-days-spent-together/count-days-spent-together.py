class Solution:
    def countDaysSpentTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        """
        Calculates total days Alice and Bob spend together in Rome.

        Complexity:
            Time: O(1) constant time calendar conversion.
            Space: O(1) auxiliary space.
        """
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]

        def to_day_of_year(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days_in_month[: month - 1]) + day

        start = max(to_day_of_year(arriveAlice), to_day_of_year(arriveBob))
        end = min(to_day_of_year(leaveAlice), to_day_of_year(leaveBob))

        return max(0, end - start + 1)

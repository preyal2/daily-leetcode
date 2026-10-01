class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Determines circular starting gas station in single-pass O(N) greedy sweep.

        Time Complexity: O(N) single-pass iteration.
        Space Complexity: O(1) constant auxiliary space.
        """
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        curr_tank = 0
        starting_station = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            total_tank += net
            curr_tank += net

            # If current tank drops below 0, cannot start anywhere up to i
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        total_surplus = 0
        current_surplus = 0
        start_index = 0
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            current_surplus += gas[i] - cost[i]
            if current_surplus < 0:
                start_index = i + 1
                current_surplus = 0
        return start_index if total_surplus >= 0 else -1
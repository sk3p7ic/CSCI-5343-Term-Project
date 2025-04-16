class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total, surplus, start = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            surplus += diff
            if surplus < 0:
                start = i + 1
                surplus = 0
        return start if total >= 0 else -1

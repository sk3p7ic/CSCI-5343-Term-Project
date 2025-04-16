class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        n = len(machines)
        total_dresses = sum(machines)
        if total_dresses % n != 0:
            return -1
        target = total_dresses // n
        max_moves = 0
        balance = 0
        for dresses in machines:
            diff = dresses - target
            balance += diff
            max_moves = max(max_moves, abs(balance), diff)
        return max_moves
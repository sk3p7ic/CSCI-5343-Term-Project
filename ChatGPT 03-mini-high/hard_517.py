class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        
        target = total // n
        moves = 0
        cumulative = 0
        
        for machine in machines:
            diff = machine - target
            cumulative += diff
            moves = max(moves, abs(cumulative), diff)
        
        return moves

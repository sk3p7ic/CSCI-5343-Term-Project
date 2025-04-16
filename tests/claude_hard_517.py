class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        
        # If total dresses cannot be evenly distributed, return -1
        if total_dresses % n != 0:
            return -1
        
        target = total_dresses // n
        
        # Max moves needed will be either:
        # 1. Maximum number of dresses that need to be moved from one machine
        # 2. The maximum difference in cumulative sum at any point (represents flow)
        max_moves = 0
        balance = 0  # Running balance of excess/deficit
        
        for machine in machines:
            # How many dresses this machine needs to give/receive
            balance += machine - target
            
            # Max moves needed is the maximum of:
            # 1. Current max moves
            # 2. Current machine's excess (how many dresses it needs to give away)
            # 3. Absolute value of balance (represents net flow at this point)
            max_moves = max(max_moves, machine - target, abs(balance))
        
        return max_moves
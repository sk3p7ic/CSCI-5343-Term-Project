class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Find the starting gas station's index to complete a circular trip.
        
        Args:
            gas: List where gas[i] is the amount of gas at station i
            cost: List where cost[i] is the gas cost to travel from station i to i+1
            
        Returns:
            The starting gas station's index, or -1 if no solution exists
        """
        # Check if there's enough total gas to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        start_index = 0
        remaining_gas = 0
        
        for i in range(len(gas)):
            # Calculate the remaining gas after visiting station i
            remaining_gas += gas[i] - cost[i]
            
            # If we can't reach the next station, start from the next station
            if remaining_gas < 0:
                start_index = i + 1
                remaining_gas = 0
        
        return start_index
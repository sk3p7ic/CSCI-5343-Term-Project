class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Determine if you can reach the last index of the array.
        
        Args:
            nums: Array where each element represents the maximum jump length
                 at that position
            
        Returns:
            True if the last index can be reached, False otherwise
        """
        # Initialize the maximum reachable position
        max_reach = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current position is beyond our reach, return False
            if i > max_reach:
                return False
                
            # Update the maximum reachable position
            max_reach = max(max_reach, i + nums[i])
            
            # If we can already reach the last index, return True
            if max_reach >= len(nums) - 1:
                return True
                
        return True
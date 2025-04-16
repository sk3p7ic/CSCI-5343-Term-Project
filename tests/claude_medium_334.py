class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Check if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
        
        Args:
            nums: Array of integers
            
        Returns:
            True if such triplet exists, False otherwise
        """
        # Initialize the first and second values to the maximum possible integer value
        first = second = float('inf')
        
        for num in nums:
            # If current number is less than or equal to first, update first
            if num <= first:
                first = num
            # If current number is less than or equal to second but greater than first, update second
            elif num <= second:
                second = num
            # If we found a number greater than both first and second, we have our triplet
            else:
                return True
                
        # No triplet found
        return False
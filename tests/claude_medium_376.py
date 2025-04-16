class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        """
        Find the length of the longest wiggle subsequence.
        
        Args:
            nums: Array of integers
            
        Returns:
            Length of the longest wiggle subsequence
        """
        if len(nums) < 2:
            return len(nums)
        
        # Initialize the length to 1 (minimum possible length)
        length = 1
        
        # Initialize the previous difference to 0
        prev_diff = 0
        
        for i in range(1, len(nums)):
            # Calculate the current difference
            curr_diff = nums[i] - nums[i-1]
            
            # If the difference is not zero and has a different sign than the previous difference,
            # or if we are just starting (prev_diff is 0), increment the length
            if (curr_diff > 0 and prev_diff <= 0) or (curr_diff < 0 and prev_diff >= 0):
                length += 1
                prev_diff = curr_diff
        
        return length
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        Arrange a list of non-negative integers to form the largest number.
        
        Args:
            nums: List of non-negative integers
            
        Returns:
            String representation of the largest possible number
        """
        # Convert integers to strings for comparison
        nums_str = [str(num) for num in nums]
        
        # Define a custom comparison function
        def compare(x, y):
            return int(y + x) - int(x + y)
        
        # Sort the numbers based on the custom comparison
        nums_str.sort(key=functools.cmp_to_key(compare))
        
        # Join the sorted strings to form the result
        result = ''.join(nums_str)
        
        # Handle the case where the result starts with '0'
        return '0' if result[0] == '0' else result
        
import functools
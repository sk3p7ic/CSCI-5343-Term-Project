class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Try to form a triangle with the largest three sides first
        # For a valid triangle, the sum of the two shorter sides must be greater than the longest side
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            
            # Check if these three sides can form a triangle
            if b + c > a:
                # Return the perimeter if a valid triangle can be formed
                return a + b + c
        
        # If no valid triangle can be formed, return 0
        return 0
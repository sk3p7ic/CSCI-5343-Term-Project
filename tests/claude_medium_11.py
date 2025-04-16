class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate width between the two lines
            width = right - left
            
            # Calculate the height of the container (limited by the shorter line)
            h = min(height[left], height[right])
            
            # Calculate area and update max_area if necessary
            current_area = width * h
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter line inward
            # (since moving the taller line would only decrease area or keep it the same)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
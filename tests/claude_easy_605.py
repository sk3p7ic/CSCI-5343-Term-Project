class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Edge case: if n is 0, we can always place 0 flowers
        if n == 0:
            return True
        
        # Create a copy to avoid modifying the input
        bed = flowerbed.copy()
        length = len(bed)
        count = 0
        
        for i in range(length):
            # Check if current plot is empty and its adjacent plots are also empty
            # (or out of bounds)
            if bed[i] == 0 and (i == 0 or bed[i-1] == 0) and (i == length-1 or bed[i+1] == 0):
                # Plant a flower
                bed[i] = 1
                count += 1
                
                # If we've planted enough flowers, return True
                if count >= n:
                    return True
        
        # If we couldn't plant n flowers, return False
        return False
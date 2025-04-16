class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, return False
        if total_sum % 3 != 0:
            return False
        
        # Target sum for each part
        target = total_sum // 3
        
        # Variables to track current sum and number of parts found
        current_sum = 0
        parts_found = 0
        
        # Iterate through the array (except the last element)
        for i in range(len(arr) - 1):
            current_sum += arr[i]
            
            # If we found a part with the target sum
            if current_sum == target:
                parts_found += 1
                current_sum = 0  # Reset the current sum
                
                # If we found 2 parts, check if the remaining elements sum to target
                if parts_found == 2:
                    # Calculate the sum of remaining elements
                    remaining_sum = sum(arr[i+1:])
                    return remaining_sum == target
        
        return False
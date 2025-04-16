class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def is_valid(max_sum):
            """Check if it's possible to split the array into k subarrays with 
            no subarray having a sum greater than max_sum."""
            count = 1  # Number of subarrays
            current_sum = 0
            
            for num in nums:
                # If a single number is greater than the max_sum, it's not possible
                if num > max_sum:
                    return False
                
                # If adding the current number exceeds max_sum, start a new subarray
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    
                    # If we need more than k subarrays, this max_sum is too small
                    if count > k:
                        return False
                else:
                    current_sum += num
            
            return True
        
        # Binary search for the minimum largest subarray sum
        left = max(nums)  # Lower bound: largest single element
        right = sum(nums)  # Upper bound: sum of the entire array
        
        while left < right:
            mid = left + (right - left) // 2
            
            if is_valid(mid):
                # If it's valid with this max_sum, try a smaller value
                right = mid
            else:
                # If not valid, we need a larger max_sum
                left = mid + 1
        
        return left
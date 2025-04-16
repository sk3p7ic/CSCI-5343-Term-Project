class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Initialize sum
        max_sum = 0
        
        # Pair adjacent elements after sorting
        # The min of each pair will be the smaller element, which is at even indices
        for i in range(0, len(nums), 2):
            max_sum += nums[i]
            
        return max_sum
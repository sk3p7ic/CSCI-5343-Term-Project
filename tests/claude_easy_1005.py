class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        # Sort the array
        nums.sort()
        
        # Step 1: Negate negative numbers first (greedy)
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        
        # Step 2: If k is still odd, negate the smallest number
        if k % 2 == 1:
            # Find the smallest number in the modified array
            min_index = nums.index(min(nums))
            nums[min_index] = -nums[min_index]
        
        # Return the sum of the modified array
        return sum(nums)
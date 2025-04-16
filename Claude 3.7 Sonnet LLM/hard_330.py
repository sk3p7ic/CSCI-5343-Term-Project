class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        i = 0  # index for nums array
        miss = 1  # the smallest number we cannot form yet
        
        while miss <= n:
            # If we can use the current number in nums
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]  # extend our coverage
                i += 1
            else:
                # We need to patch the 'miss' number
                patches += 1
                miss += miss  # by adding 'miss', we can now form all sums up to 2*miss-1
        
        return patches
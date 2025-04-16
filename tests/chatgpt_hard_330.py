class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        missing = 1
        i = 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                patches += 1
        return patches

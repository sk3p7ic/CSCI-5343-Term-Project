class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        reachable = 0
        i = 0
        while reachable < n:
            if i < len(nums) and nums[i] <= reachable + 1:
                reachable += nums[i]
                i += 1
            else:
                reachable += reachable + 1
                patches += 1
        return patches
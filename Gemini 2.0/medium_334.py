class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        min1 = float('inf')
        min2 = float('inf')

        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True

        return False
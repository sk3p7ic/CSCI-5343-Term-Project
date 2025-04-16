class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        for i in range(min(k, n)):
            if nums[i] < 0:
                nums[i] = -nums[i]
            else:
                break

        remaining_k = k - min(k, n)
        if remaining_k > 0 and remaining_k % 2 == 1:
            min_abs = min(abs(x) for x in nums)
            for i in range(n):
                if abs(nums[i]) == min_abs:
                    nums[i] = -nums[i]
                    break

        return sum(nums)
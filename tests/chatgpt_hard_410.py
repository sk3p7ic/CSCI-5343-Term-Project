class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(maxSum: int) -> bool:
            count, curr = 1, 0
            for num in nums:
                if curr + num > maxSum:
                    count += 1
                    curr = num
                    if count > k:
                        return False
                else:
                    curr += num
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left

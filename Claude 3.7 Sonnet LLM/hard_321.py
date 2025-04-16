class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        m, n = len(nums1), len(nums2)
        # Try all possible combinations: take i elements from nums1 and k-i from nums2
        return max(
            self.merge(self.maxSingleArray(nums1, i), self.maxSingleArray(nums2, k - i))
            for i in range(max(0, k - n), min(k, m) + 1)
        )
    
    def maxSingleArray(self, nums: list[int], k: int) -> list[int]:
        """Create the maximum number of length k from a single array."""
        stack = []
        # Number of elements we can drop
        to_drop = len(nums) - k
        
        for num in nums:
            # Pop elements from stack if current number is larger and we can afford to drop
            while stack and stack[-1] < num and to_drop > 0:
                stack.pop()
                to_drop -= 1
            stack.append(num)
        
        # If we couldn't drop enough elements, trim the end
        return stack[:k]
    
    def merge(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Merge two arrays to get the maximum number."""
        result = []
        while nums1 or nums2:
            # Pick the array that will contribute the larger sequence
            if nums1 > nums2:
                result.append(nums1[0])
                nums1 = nums1[1:]
            else:
                result.append(nums2[0])
                nums2 = nums2[1:]
        return result
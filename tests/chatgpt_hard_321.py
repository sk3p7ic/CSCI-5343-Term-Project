class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def pick(nums: list[int], pick_count: int) -> list[int]:
            drop = len(nums) - pick_count
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:pick_count]
        
        def merge(nums1: list[int], nums2: list[int]) -> list[int]:
            merged = []
            while nums1 or nums2:
                # Lexicographical comparison: list comparison works as desired.
                if nums1 > nums2:
                    merged.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    merged.append(nums2[0])
                    nums2 = nums2[1:]
            return merged

        max_sequence = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end + 1):
            part1 = pick(nums1, i)
            part2 = pick(nums2, k - i)
            candidate = merge(part1, part2)
            if candidate > max_sequence:
                max_sequence = candidate
        return max_sequence

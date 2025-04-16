class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max_subsequence(nums, length):
            stack = []
            drop = len(nums) - length
            for num in nums:
                while stack and drop > 0 and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]

        def merge(sub1, sub2):
            merged = []
            i = 0
            j = 0
            while i < len(sub1) or j < len(sub2):
                if j == len(sub2) or (i < len(sub1) and sub1[i:] > sub2[j:]):
                    merged.append(sub1[i])
                    i += 1
                else:
                    merged.append(sub2[j])
                    j += 1
            return merged

        max_merged = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)
            merged = merge(sub1, sub2)
            if not max_merged or merged > max_merged:
                max_merged = merged

        return max_merged
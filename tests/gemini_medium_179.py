from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(n1, n2):
            s1 = str(n1)
            s2 = str(n2)
            if s1 + s2 > s2 + s1:
                return -1
            elif s1 + s2 < s2 + s1:
                return 1
            else:
                return 0

        sorted_nums = sorted(nums, key=cmp_to_key(compare))
        result = "".join(map(str, sorted_nums))
        return "0" if result[0] == "0" else result
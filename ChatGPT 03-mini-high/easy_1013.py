class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        current_sum = 0
        partitions = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum == target:
                partitions += 1
                current_sum = 0
                if partitions == 2 and i < len(arr) - 1:
                    return True
        return False
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        k = len(nums)
        pq = []
        max_val = -float('inf')

        for i in range(k):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        min_range = float('inf')
        result = [-float('inf'), float('inf')]

        while True:
            min_val, list_index, element_index = heapq.heappop(pq)

            if max_val - min_val < min_range:
                min_range = max_val - min_val
                result = [min_val, max_val]

            if element_index + 1 < len(nums[list_index]):
                next_val = nums[list_index][element_index + 1]
                max_val = max(max_val, next_val)
                heapq.heappush(pq, (next_val, list_index, element_index + 1))
            else:
                break

        return result
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        current_max = float('-inf')
        
        # Initialize the heap with the first element of each list.
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], 0, i))
            current_max = max(current_max, lst[0])
        
        best_range = [heap[0][0], current_max]
        best_size = current_max - heap[0][0]
        
        while True:
            current_min, idx, list_id = heapq.heappop(heap)
            
            # Update the best range if the current range is smaller.
            if current_max - current_min < best_size:
                best_range = [current_min, current_max]
                best_size = current_max - current_min
            
            # If the current list is exhausted, stop the process.
            if idx + 1 == len(nums[list_id]):
                break
            
            # Add the next element from the same list.
            next_val = nums[list_id][idx + 1]
            heapq.heappush(heap, (next_val, idx + 1, list_id))
            current_max = max(current_max, next_val)
        
        return best_range

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        import heapq
        
        # Initialize the heap with the first element from each list
        # Format: (value, list_index, element_index)
        min_heap = []
        max_val = float('-inf')
        
        # Initialize with the first element from each list
        for i, lst in enumerate(nums):
            if lst:  # Make sure the list is not empty
                heapq.heappush(min_heap, (lst[0], i, 0))
                max_val = max(max_val, lst[0])
        
        # Initialize the smallest range
        smallest_range = [float('-inf'), float('inf')]
        smallest_range_size = float('inf')
        
        # Process the heap
        while len(min_heap) == len(nums):  # Ensure we have one element from each list
            min_val, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Calculate current range
            current_range_size = max_val - min_val
            
            # Update smallest range if current range is smaller
            if current_range_size < smallest_range_size:
                smallest_range = [min_val, max_val]
                smallest_range_size = current_range_size
            
            # Move to the next element in the same list if possible
            if elem_idx + 1 < len(nums[list_idx]):
                next_elem = nums[list_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
                max_val = max(max_val, next_elem)
            else:
                # If we've exhausted a list, we can't form ranges with elements from all lists
                break
        
        return smallest_range
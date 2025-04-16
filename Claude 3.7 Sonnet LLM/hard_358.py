class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # Special case: if k is 0, no constraint on arrangement
        if k == 0:
            return s
            
        # Count frequencies of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Create a max heap based on character frequency
        import heapq
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        # Keep track of characters that are in the "cooldown" period
        cooldown_queue = []
        
        while max_heap:
            # Get the most frequent character available
            neg_count, char = heapq.heappop(max_heap)
            result.append(char)
            neg_count += 1  # Decrease count (remember it's negative)
            
            # Add the used character to cooldown queue with its updated count
            if neg_count < 0:  # If we still have occurrences left
                cooldown_queue.append((neg_count, char))
            
            # Check if any character from cooldown can be released
            if len(cooldown_queue) >= k:
                next_available = cooldown_queue.pop(0)
                heapq.heappush(max_heap, next_available)
        
        # If we couldn't place all characters, return empty string
        if len(result) < len(s):
            return ""
        
        return "".join(result)
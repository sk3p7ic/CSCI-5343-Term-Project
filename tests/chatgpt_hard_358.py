import heapq
from collections import Counter

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        result = []
        
        while max_heap:
            temp = []
            count_popped = 0
            # Try to pop up to k elements for the current round
            for _ in range(k):
                if not max_heap:
                    break
                freq, char = heapq.heappop(max_heap)
                result.append(char)
                count_popped += 1
                if -freq > 1:
                    temp.append((freq + 1, char))
            # Push the used characters back into the heap
            for item in temp:
                heapq.heappush(max_heap, item)
            # If we haven't finished building the result and didn't pop k elements,
            # it means we cannot satisfy the distance constraint.
            if max_heap and count_popped < k:
                return ""
        
        return "".join(result)

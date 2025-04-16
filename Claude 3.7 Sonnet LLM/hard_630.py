class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # Sort courses by their end date (lastDay)
        courses.sort(key=lambda x: x[1])
        
        import heapq
        total_time = 0
        max_heap = []  # Max heap to store course durations
        
        for duration, lastDay in courses:
            # If we can add this course without exceeding its lastDay
            if total_time + duration <= lastDay:
                heapq.heappush(max_heap, -duration)  # Use negative for max heap
                total_time += duration
            # If we've already taken some longer course, replace it with current one
            elif max_heap and -max_heap[0] > duration:
                # Remove the longest course we've taken so far
                longest_duration = -heapq.heappop(max_heap)
                
                # Add current course and update total time
                total_time = total_time - longest_duration + duration
                heapq.heappush(max_heap, -duration)
        
        # Number of courses we can take is the size of our heap
        return len(max_heap)
import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # Sort the courses by their last day
        courses.sort(key=lambda x: x[1])
        total_time = 0
        max_heap = []  # Using a max-heap (by pushing negative durations)
        
        for duration, last_day in courses:
            if total_time + duration <= last_day:
                total_time += duration
                heapq.heappush(max_heap, -duration)
            elif max_heap and -max_heap[0] > duration:
                total_time += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)
        
        return len(max_heap)

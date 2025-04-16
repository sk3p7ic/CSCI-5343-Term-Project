import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # Sort courses by their last day
        heap = []  # Max heap to store the durations of taken courses
        current_time = 0
        taken_courses = 0

        for duration, last_day in courses:
            if current_time + duration <= last_day:
                heapq.heappush(heap, -duration)
                current_time += duration
                taken_courses += 1
            elif heap and -heap[0] > duration:
                longest_duration = -heapq.heappop(heap)
                current_time -= longest_duration
                current_time += duration
                heapq.heappush(heap, -duration)

        return taken_courses
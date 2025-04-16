from collections import Counter
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        counts = Counter(s)
        pq = [(-count, char) for char, count in counts.items()]
        heapq.heapify(pq)
        result = []
        wait_list = []

        while pq:
            count, char = heapq.heappop(pq)
            result.append(char)
            counts[char] -= 1
            wait_list.append((char, len(result) + k))

            while wait_list and wait_list[0][1] == len(result):
                prev_char, _ = wait_list.pop(0)
                if counts[prev_char] > 0:
                    heapq.heappush(pq, (-counts[prev_char], prev_char))

        return "".join(result) if len(result) == len(s) else ""
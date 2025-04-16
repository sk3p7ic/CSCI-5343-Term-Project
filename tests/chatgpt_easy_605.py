class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        while i < length and n > 0:
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    i += 1  # Skip the next plot to avoid adjacent planting
            i += 1
        return n == 0

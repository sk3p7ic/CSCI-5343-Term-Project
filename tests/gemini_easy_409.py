class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        length = 0
        has_odd = False
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True

        if has_odd:
            length += 1

        return length
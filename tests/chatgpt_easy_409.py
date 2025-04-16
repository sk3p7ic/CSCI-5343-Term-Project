class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        length = 0
        odd_found = False
        
        for count in counts.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                odd_found = True
        
        return length + 1 if odd_found else length

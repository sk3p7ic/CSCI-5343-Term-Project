class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count frequency of each character
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Calculate the length of the longest palindrome
        length = 0
        odd_count = 0
        
        for count in char_count.values():
            # For each character, we can use an even number of occurrences
            if count % 2 == 0:
                length += count
            else:
                # For odd counts, we can use (count-1) characters and potentially
                # place one character in the middle of the palindrome
                length += count - 1
                odd_count = 1
        
        # If there was at least one character with odd count,
        # we can place one in the middle
        return length + odd_count
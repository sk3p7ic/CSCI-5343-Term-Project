class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a substring is a palindrome
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # Initialize pointers for the main check
        left, right = 0, len(s) - 1
        
        # Scan from both ends
        while left < right:
            # If characters don't match
            if s[left] != s[right]:
                # Try removing character at left or right position
                # and check if the remaining string is a palindrome
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
            
            # Move pointers inward
            left += 1
            right -= 1
        
        # If we get here without returning, the string is already a palindrome
        return True
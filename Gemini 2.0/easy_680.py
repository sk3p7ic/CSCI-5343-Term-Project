class Solution:
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try deleting the left character
                sub_left = s[left + 1:right + 1]
                if self.is_palindrome(sub_left):
                    return True
                # Try deleting the right character
                sub_right = s[left:right]
                if self.is_palindrome(sub_right):
                    return True
                return False
            left += 1
            right -= 1
        return True
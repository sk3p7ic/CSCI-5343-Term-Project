class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Remove duplicate letters to form the lexicographically smallest string 
        where each letter appears once.
        
        Args:
            s: Input string consisting of lowercase English letters
            
        Returns:
            Lexicographically smallest string with no duplicate letters
        """
        # Keep track of the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Keep track of characters we've already included in our result
        seen = set()
        
        # Use a stack to build our result
        stack = []
        
        for idx, char in enumerate(s):
            # Skip if we've already included this character
            if char in seen:
                continue
                
            # If the current character is smaller than the last character in the stack,
            # and the last character appears later in the string, we can pop it and use it later
            while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
                
            # Add current character to result
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)
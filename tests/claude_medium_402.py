class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Return the smallest possible integer after removing k digits from num.
        
        Args:
            num: A string representing a non-negative integer
            k: Number of digits to remove
            
        Returns:
            The smallest possible integer as a string after removing k digits
        """
        # Use a stack to build our result
        stack = []
        
        # Process each digit
        for digit in num:
            # While we still need to remove digits and the stack is not empty
            # and the current digit is smaller than the last digit in the stack
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            # Add the current digit to our stack
            stack.append(digit)
        
        # If we still need to remove digits, remove from the end
        # (This happens when the digits are in increasing order)
        if k > 0:
            stack = stack[:-k]
        
        # Join the stack elements to get the result
        result = ''.join(stack)
        
        # Remove leading zeros
        result = result.lstrip('0')
        
        # Return '0' if the result is an empty string
        return result if result else '0'
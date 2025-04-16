class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        # Initialize low and high pointers
        low = 0
        high = n
        
        # Initialize the result array
        result = []
        
        # Process each character in the string
        for char in s:
            if char == 'I':
                # If current character is 'I', add the smallest available number
                result.append(low)
                low += 1
            else:  # char == 'D'
                # If current character is 'D', add the largest available number
                result.append(high)
                high -= 1
        
        # Append the remaining number (low and high should be equal at this point)
        result.append(low)
        
        return result
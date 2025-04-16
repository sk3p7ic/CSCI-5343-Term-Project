class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Sort both arrays
        g.sort()  # Sort children's greed factors
        s.sort()  # Sort cookie sizes
        
        child_index = 0
        cookie_index = 0
        
        # Count how many children we can satisfy
        content_children = 0
        
        # Iterate through cookies and children
        while child_index < len(g) and cookie_index < len(s):
            # If current cookie can satisfy current child
            if s[cookie_index] >= g[child_index]:
                content_children += 1
                child_index += 1  # Move to next child
            
            # Move to next cookie regardless
            # (either we used this cookie or it was too small)
            cookie_index += 1
        
        return content_children
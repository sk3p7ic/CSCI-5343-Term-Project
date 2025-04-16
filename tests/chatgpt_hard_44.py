class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        star_idx, s_tmp_idx = -1, -1
        
        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star_idx = j
                s_tmp_idx = i
                j += 1
            elif star_idx != -1:
                j = star_idx + 1
                s_tmp_idx += 1
                i = s_tmp_idx
            else:
                return False
        
        while j < len(p) and p[j] == '*':
            j += 1
            
        return j == len(p)

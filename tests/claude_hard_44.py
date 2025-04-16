class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Optimize pattern by reducing consecutive '*' to a single '*'
        i = 0
        new_p = []
        while i < len(p):
            if p[i] == '*':
                new_p.append('*')
                while i < len(p) and p[i] == '*':
                    i += 1
            else:
                new_p.append(p[i])
                i += 1
        p = ''.join(new_p)
        
        # DP solution - dp[i][j] represents if s[0:i] matches p[0:j]
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Empty string can match with pattern containing only '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match empty sequence (dp[i][j-1]) or any sequence (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single character or characters match exactly
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]
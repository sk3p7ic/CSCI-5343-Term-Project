class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low, high = 0, len(s)
        ans = []
        for ch in s:
            if ch == 'I':
                ans.append(low)
                low += 1
            else:  # ch == 'D'
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans

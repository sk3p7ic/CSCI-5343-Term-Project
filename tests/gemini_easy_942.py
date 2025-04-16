class Solution:
    def reconstructPermutation(self, s: str) -> list[int]:
        n = len(s)
        perm = [0] * (n + 1)
        low = 0
        high = n
        for i in range(n):
            if s[i] == 'I':
                perm[i] = low
                low += 1
            else:
                perm[i] = high
                high -= 1
        perm[n] = low  # or high, as low will be equal to high at this point
        return perm
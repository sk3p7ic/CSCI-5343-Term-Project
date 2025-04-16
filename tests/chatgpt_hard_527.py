class Solution:
    def wordsAbbreviation(self, words: list[str]) -> list[str]:
        n = len(words)
        ans = [""] * n
        prefix = [1] * n  # minimum prefix length for each word

        # Group words by (first character, last character, length)
        groups = {}
        for i, word in enumerate(words):
            key = (word[0], word[-1], len(word))
            groups.setdefault(key, []).append(i)

        # Helper function to compute common prefix length between two strings
        def common_prefix(a: str, b: str) -> int:
            l = min(len(a), len(b))
            i = 0
            while i < l and a[i] == b[i]:
                i += 1
            return i

        # For each group, update the required prefix length for each word in the group
        for indices in groups.values():
            if len(indices) < 2:
                continue
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    idx1, idx2 = indices[i], indices[j]
                    cp = common_prefix(words[idx1], words[idx2])
                    prefix[idx1] = max(prefix[idx1], cp + 1)
                    prefix[idx2] = max(prefix[idx2], cp + 1)

        # Build the abbreviation for each word using the computed prefix length
        for i, word in enumerate(words):
            # If abbreviation does not shorten the word, keep the original word
            if prefix[i] >= len(word) - 2:
                ans[i] = word
            else:
                abbr = word[:prefix[i]] + str(len(word) - prefix[i] - 1) + word[-1]
                ans[i] = abbr if len(abbr) < len(word) else word

        return ans

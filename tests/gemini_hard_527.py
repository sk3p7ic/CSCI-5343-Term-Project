from collections import defaultdict

class Solution:
    def minimizeAbbreviations(self, words: list[str]) -> list[str]:
        n = len(words)
        if n <= 1:
            return words

        abbrevs = [self.abbreviate(word, 1) for word in words]

        while True:
            counts = defaultdict(list)
            for i, abbrev in enumerate(abbrevs):
                counts[abbrev].append(i)

            collisions = False
            for abbrev_indices in counts.values():
                if len(abbrev_indices) > 1:
                    collisions = True
                    for index in abbrev_indices:
                        abbrevs[index] = self.abbreviate(words[index], len(abbrevs[index]) - 2 + 1)
                    break
            if not collisions:
                break

        result = []
        for i, word in enumerate(words):
            if len(abbrevs[i]) >= len(word):
                result.append(word)
            else:
                result.append(abbrevs[i])

        return result

    def abbreviate(self, word: str, prefix_len: int) -> str:
        n = len(word)
        if prefix_len >= n - 1:
            return word
        return word[:prefix_len] + str(n - prefix_len - 1) + word[-1]
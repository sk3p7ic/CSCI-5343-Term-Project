class Solution:
    def wordsAbbreviation(self, words: list[str]) -> list[str]:
        # Function to get initial abbreviation
        def get_abbr(word, prefix_len):
            if len(word) - prefix_len - 1 <= 1:  # Not worth abbreviating
                return word
            return word[:prefix_len] + str(len(word) - prefix_len - 1) + word[-1]
        
        n = len(words)
        result = [""] * n
        
        # Initialize with prefix length of 1
        prefix_len = [1] * n
        
        # Initial abbreviations
        for i in range(n):
            result[i] = get_abbr(words[i], prefix_len[i])
        
        # Group words by their current abbreviation
        for i in range(n):
            while True:
                duplicates = []
                
                # Find all words with the same abbreviation
                for j in range(n):
                    if i != j and result[i] == result[j]:
                        duplicates.append(j)
                
                # If no duplicates found, this abbreviation is unique
                if not duplicates:
                    break
                
                # Add current word to the list of duplicates for processing
                duplicates.append(i)
                
                # Increase prefix length for all duplicates
                for j in duplicates:
                    prefix_len[j] += 1
                    result[j] = get_abbr(words[j], prefix_len[j])
        
        return result
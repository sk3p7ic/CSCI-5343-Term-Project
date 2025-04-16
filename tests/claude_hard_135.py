class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Calculate the minimum number of candies needed to distribute to children
        based on their ratings.
        
        Args:
            ratings: List of integers representing the ratings of each child
            
        Returns:
            Minimum number of candies needed
        """
        n = len(ratings)
        # Initialize each child with 1 candy
        candies = [1] * n
        
        # First pass: from left to right
        # If the current child has a higher rating than the previous one,
        # give them one more candy than the previous child
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Second pass: from right to left
        # If the current child has a higher rating than the next one,
        # ensure they have at least one more candy than the next child
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Sum up the total number of candies
        return sum(candies)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculate the maximum profit from buying and selling stocks.
        
        Args:
            prices: List of stock prices where prices[i] is the price on day i
            
        Returns:
            Maximum possible profit
        """
        max_profit = 0
        
        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the current price is higher than the previous day's price,
            # we can make a profit by buying on the previous day and selling today
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                
        return max_profit
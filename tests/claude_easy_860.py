class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # Keep track of the number of $5 and $10 bills we have
        five_count = 0
        ten_count = 0
        
        for bill in bills:
            if bill == 5:
                # Customer pays with $5, no change needed
                five_count += 1
            elif bill == 10:
                # Customer pays with $10, need to give $5 back
                if five_count == 0:
                    return False  # Can't provide change
                five_count -= 1
                ten_count += 1
            else:  # bill == 20
                # Customer pays with $20, need to give $15 back
                # Option 1: Give one $10 and one $5 (preferred if available)
                if ten_count >= 1 and five_count >= 1:
                    ten_count -= 1
                    five_count -= 1
                # Option 2: Give three $5 bills
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False  # Can't provide change
        
        # If we've processed all customers successfully, return True
        return True
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        """
        Reconstruct the queue based on people's heights and positions.
        
        Args:
            people: List where people[i] = [hi, ki] represents the ith person of height hi with
                   exactly ki other people in front who have height >= hi
            
        Returns:
            Reconstructed queue where each position satisfies the height and position requirements
        """
        # Sort people by height (descending) and when heights are equal, sort by k (ascending)
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Initialize an empty result list
        result = []
        
        # Insert each person at their k position
        for person in people:
            result.insert(person[1], person)
            
        return result
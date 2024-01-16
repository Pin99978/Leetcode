
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        max_i = max(candies)
    
        result = []
        for i in candies:
            if  i + extraCandies >= max_i :                
                result.append(True)
            else:                
                result.append(False)            
        return result

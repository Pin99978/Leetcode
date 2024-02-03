#44ms 
# O(n^2) -> 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # go with hash

        counter = {}
        rev_counter={}
        for i in arr:  # ( O(n) )

            if i not in counter:
                counter[i] = 1 # ( O(n) )
            else :
                counter[i] +=1

        for i ,val in counter.items():

            if val not in rev_counter:

                rev_counter[val] = 1
            else:
                return False 
        
        return True

            
                        

            

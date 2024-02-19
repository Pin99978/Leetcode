
# pure bitwise operation
# 38ms / 16.56 MB
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        cnt  = 0
        # always check LSB with 1  // 1001 & 0001 -> 0001 
        while n != 0 :
            
            if n & 1 == 1:
              
                cnt += 1
            # right shift op
            n >>= 1
        return cnt    

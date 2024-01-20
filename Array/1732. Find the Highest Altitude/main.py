# Time: 34ms O(n) > 90.71%  Space :16.54mb > 55.55%

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        cur_alt , max_alt = 0 , 0

        for i in gain:

            cur_alt += i
            if cur_alt > max_alt:

                max_alt = cur_alt
            
        return max_alt

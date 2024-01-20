# time O(n) 874ms (95%) Memory 28.4MB (56.x%)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) ==k:
            return sum(nums) / k
               
        pt1 = 0
        pt2 = k
        # get the first max result
        max_sum = sum(nums[pt1 : pt2])
        cur_sum = max_sum
        while pt2 < len(nums) :
          
            cur_sum = cur_sum - nums[pt1] + nums[pt2]
            if ( cur_sum > max_sum ):
                max_sum = cur_sum
            pt2+=1
            pt1+=1 
        return max_sum / k

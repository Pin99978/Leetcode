# time : O(n)  , space : 17.72mB

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        
        left_s = 0
        right_s = sum(nums) - nums[0] # O(n)

        if left_s == right_s:
            return 0 

        for i in range(1, len(nums)): # O(n)
            
            left_s += nums[i-1]
            right_s -= ( nums[i]  )
           
            if left_s == right_s :               
                return i
            if i ==len(nums)-1 and left_s != right_s:
                return -1



            

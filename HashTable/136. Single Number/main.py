
#Runtime 117 ms
#54.76%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) ==1 :
            return nums[0]


        record = {}

        for i in nums:

            if i in record:
                record[i] += 1
            else:
                record[i] =1
            
        for key ,val in record.items():

            if val == 1:

                return key

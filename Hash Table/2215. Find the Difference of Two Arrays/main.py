# Runtime 144 ms
# beats 68.53%

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        l2 = []
        l1 = []
        dict1= { i : True for i in nums1  }
        dict2 ={ i : True for i in nums2  }
        
        for i in set(nums1):

            try :
                dict2[i] 
            except :  
                l1.append(i)

        for i in set(nums2):
            try:  
                dict1[i]  
            except:
                l2.append(i)
        return [l1 , l2]

class Solution(object):
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # [ None , 1 , 2, None]

        prev = None
        cur = head
        while cur != None:
           
            head = head.next
            cur.next = prev
            prev = cur
            cur = head
        return prev


            
            
            
        

        
          

            

            
   

        

        

        
        
        
    
        

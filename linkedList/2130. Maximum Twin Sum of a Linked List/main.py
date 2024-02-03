class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # two node to move the middle and middle + 1
        prev = None
        slow = head
        fast = head
        fast = fast.next.next

        while fast and fast.next :

            head = head.next
            slow.next =prev
            prev = slow
            slow = head
            
            fast = fast.next.next
        
           
        # move once two next stage 
        head = head.next
        slow.next =prev
        prev = slow
        slow = head
        

        maximum = prev.val + slow.val
        while prev.next != None :

            prev = prev.next 
            slow = slow.next
            cur_max = prev.val + slow.val
            if ( cur_max > maximum):
                maximum = cur_max
            
        return maximum

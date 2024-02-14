# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 47ms 

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None
        
        dummy = ListNode()
        
        dummy.next = head
        dummy.val = None
        # special case if first element is equal to val
        #while head.val == val:
        #    head = head.next
        #    if head == None:
        #        return None

        tmp  = dummy
        prev = dummy 
        
        while dummy :

            if dummy.val == val:
                
                dummy = prev
               
                dummy.next = dummy.next.next
                
            prev = dummy
            
            dummy = dummy.next
            
        return tmp.next

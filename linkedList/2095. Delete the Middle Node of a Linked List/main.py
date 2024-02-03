# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) -> 646ms ( > 47.87% )

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # if head.next = None
        
        if head.next ==None or head ==None:
            
            return  None

        # go through the full node and determine the length
        i = 0
        tmp = head       
        while  head != None :
            
            head = head.next
            i += 1 
        
        middle = i // 2         
        start = 0 
        # move head back to inital node
        head = tmp

        
        # move the node to the middle - 1 node  
        while  start < middle - 1  :
            tmp = tmp.next
            start +=1
            
        #now start at the head -1 node
        tmp.next =tmp.next.next
        
        return head
        

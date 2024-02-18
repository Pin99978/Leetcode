# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#34ms 16.53mb

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        prev = None
        cur  = head

        # reversed the LinkedList first
        while cur:
            
            head = head.next
            cur.next = prev
            prev = cur
            cur = head

        rev = prev
        i = 0 
        deci = 0

        # go with bitwise left shift 
        # 1:0 
        # 1(1)  << 1  // 2(10)
        # 2(10) << 1  // 4(100)
        # 4(100)<< 1  // 8(1000)
        while rev:
            deci += rev.val * (1<<i)
            
            rev =rev.next
            i += 1
        return deci
# this method 
class Solution:
    def runwithandOperation(self, head: ListNode) -> int:
        
        
        # store to str then covert it to binary

        decimal_str = ""
        while head:
            decimal_str+= str(head.val)
            head  = head.next
        
        binary = int(decimal_str , 2)
        base = 1
        decimal = 0
        while binary> 0:
            if binary & 1:
                decimal += base
            binary >>= 1
            base <<= 1 
        return decimal

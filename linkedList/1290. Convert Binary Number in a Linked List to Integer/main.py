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
